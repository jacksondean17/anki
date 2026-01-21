#!/usr/bin/env python3
"""
Generate an Anki deck for San Francisco neighborhoods using real map data.
Each card shows a map with a highlighted neighborhood on the front,
and the neighborhood name on the back.
"""

import genanki
import os
import requests
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import contextily as ctx

def download_neighborhoods():
    """Download SF neighborhoods GeoJSON from GitHub."""
    print("Downloading SF neighborhood data from GitHub...")

    # Try multiple sources in case one fails
    urls = [
        "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/san-francisco.geojson",
        "https://raw.githubusercontent.com/blackmad/neighborhoods/master/san-francisco.geojson",
    ]

    for url in urls:
        try:
            print(f"Trying {url.split('/')[-3]}...")
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            with open('sf_neighborhoods.geojson', 'w') as f:
                f.write(response.text)

            print("✓ Downloaded neighborhood data")
            gdf = gpd.read_file('sf_neighborhoods.geojson')

            # Check if data has the expected structure
            if 'name' not in gdf.columns:
                # Try finding a column with neighborhood names
                name_col = None
                for col in gdf.columns:
                    if 'name' in col.lower() or 'neigh' in col.lower():
                        name_col = col
                        break
                if name_col:
                    gdf = gdf.rename(columns={name_col: 'nhood'})
            else:
                gdf = gdf.rename(columns={'name': 'nhood'})

            return gdf

        except Exception as e:
            print(f"  Failed: {e}")
            continue

    raise Exception("Could not download neighborhood data from any source")

def create_neighborhood_map(gdf, neighborhood_name, output_path):
    """Create a map image with one neighborhood highlighted."""
    fig, ax = plt.subplots(figsize=(10, 12))

    # Reproject to Web Mercator for basemap
    gdf_projected = gdf.to_crs(epsg=3857)

    # Find the specific neighborhood
    target = gdf_projected[gdf_projected['nhood'] == neighborhood_name]

    if len(target) == 0:
        print(f"Warning: Neighborhood '{neighborhood_name}' not found")
        return False

    # Plot all neighborhoods in light gray
    gdf_projected.boundary.plot(ax=ax, linewidth=1, edgecolor='gray', alpha=0.5)
    gdf_projected.plot(ax=ax, color='lightgray', alpha=0.3)

    # Highlight the target neighborhood
    target.plot(ax=ax, color='#FF4444', alpha=0.7, edgecolor='darkred', linewidth=2)

    # Add basemap
    try:
        ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron, zoom=12)
    except Exception as e:
        print(f"Note: Could not add basemap: {e}")

    # Remove axis labels
    ax.set_axis_off()

    # Add title
    plt.title("Which San Francisco neighborhood is highlighted?",
              fontsize=16, fontweight='bold', pad=20)

    # Save with tight layout
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

    return True

def generate_deck():
    """Generate the Anki deck with real maps."""

    # Download neighborhood data
    gdf = download_neighborhoods()

    print(f"Found {len(gdf)} neighborhoods in dataset")
    print("\nNeighborhoods available:")
    for idx, name in enumerate(sorted(gdf['nhood'].unique()), 1):
        print(f"  {idx}. {name}")

    # Create images directory
    os.makedirs('images_real', exist_ok=True)

    # Create model for the neighborhood cards
    neighborhood_model = genanki.Model(
        1607392320,  # Different model ID
        'SF Neighborhood Model (Real Maps)',
        fields=[
            {'name': 'Image'},
            {'name': 'Neighborhood'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '<div style="text-align: center;">{{Image}}</div>',
                'afmt': '{{FrontSide}}<hr id="answer"><div style="text-align: center; font-size: 24px; font-weight: bold;">{{Neighborhood}}</div>',
            },
        ],
        css="""
            .card {
                font-family: arial;
                font-size: 20px;
                text-align: center;
                color: black;
                background-color: white;
            }
            img {
                max-width: 95%;
                max-height: 500px;
            }
        """
    )

    # Create deck
    deck = genanki.Deck(
        2059400111,  # Different deck ID
        'San Francisco Neighborhoods (Real Maps)'
    )

    media_files = []
    successful_neighborhoods = []

    # Generate a map for each neighborhood
    print("\nGenerating maps...")
    for neighborhood in sorted(gdf['nhood'].unique()):
        filename = f"{neighborhood.replace(' ', '_').replace('/', '-').lower()}.png"
        filepath = os.path.join('images_real', filename)

        print(f"  Creating map for {neighborhood}...")
        success = create_neighborhood_map(gdf, neighborhood, filepath)

        if success:
            media_files.append(filepath)
            successful_neighborhoods.append(neighborhood)

            # Create note
            note = genanki.Note(
                model=neighborhood_model,
                fields=[
                    f'<img src="{filename}">',
                    neighborhood
                ]
            )
            deck.add_note(note)

    # Generate package
    print("\nCreating Anki package...")
    package = genanki.Package(deck)
    package.media_files = media_files
    package.write_to_file('sf_neighborhoods_real.apkg')

    print(f"\n✓ Created deck with {len(successful_neighborhoods)} neighborhoods")
    print(f"✓ Generated {len(media_files)} map images")
    print(f"✓ Deck saved as: sf_neighborhoods_real.apkg")

if __name__ == '__main__':
    generate_deck()
