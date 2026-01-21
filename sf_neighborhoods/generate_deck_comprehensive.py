#!/usr/bin/env python3
"""
Generate a comprehensive Anki deck for San Francisco neighborhoods.
Combines existing data with manually added key neighborhoods.
"""

import genanki
import os
import requests
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import contextily as ctx

def download_base_neighborhoods():
    """Download base SF neighborhoods GeoJSON from GitHub."""
    print("Downloading base SF neighborhood data...")

    urls = [
        "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/san-francisco.geojson",
        "https://raw.githubusercontent.com/blackmad/neighborhoods/master/san-francisco.geojson",
    ]

    for url in urls:
        try:
            print(f"Trying {url.split('/')[-3]}...")
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            with open('sf_neighborhoods_base.geojson', 'w') as f:
                f.write(response.text)

            print("✓ Downloaded base neighborhood data")
            return gpd.read_file('sf_neighborhoods_base.geojson')

        except Exception as e:
            print(f"  Failed: {e}")
            continue

    raise Exception("Could not download neighborhood data")

def add_missing_neighborhoods(gdf):
    """Add key missing neighborhoods by subdividing or creating new boundaries."""
    print("\nAdding missing key neighborhoods...")

    new_neighborhoods = []

    # Mission Bay - carved from South of Market (eastern part near the bay)
    soma = gdf[gdf['name'] == 'South of Market']
    if not soma.empty:
        soma_geom = soma.geometry.iloc[0]
        # Create Mission Bay as eastern portion of SoMa
        mission_bay_coords = [
            (-122.395, 37.775),
            (-122.390, 37.775),
            (-122.387, 37.770),
            (-122.387, 37.765),
            (-122.395, 37.765),
            (-122.395, 37.775)
        ]
        mission_bay_poly = Polygon(mission_bay_coords)
        intersection = mission_bay_poly.intersection(soma_geom)
        if not intersection.is_empty:
            new_neighborhoods.append({
                'name': 'Mission Bay',
                'geometry': intersection
            })
            print("  ✓ Added Mission Bay")

    # Dogpatch - between Potrero Hill and the waterfront
    dogpatch_coords = [
        (-122.395, 37.765),
        (-122.388, 37.765),
        (-122.388, 37.755),
        (-122.395, 37.755),
        (-122.395, 37.765)
    ]
    new_neighborhoods.append({
        'name': 'Dogpatch',
        'geometry': Polygon(dogpatch_coords)
    })
    print("  ✓ Added Dogpatch")

    # Hayes Valley - carved from Western Addition/Downtown area
    hayes_valley_coords = [
        (-122.425, 37.777),
        (-122.420, 37.777),
        (-122.420, 37.772),
        (-122.425, 37.772),
        (-122.425, 37.777)
    ]
    new_neighborhoods.append({
        'name': 'Hayes Valley',
        'geometry': Polygon(hayes_valley_coords)
    })
    print("  ✓ Added Hayes Valley")

    # Tenderloin - carved from Downtown/Civic Center
    tenderloin_coords = [
        (-122.419, 37.788),
        (-122.408, 37.788),
        (-122.408, 37.780),
        (-122.419, 37.780),
        (-122.419, 37.788)
    ]
    new_neighborhoods.append({
        'name': 'Tenderloin',
        'geometry': Polygon(tenderloin_coords)
    })
    print("  ✓ Added Tenderloin")

    # NOPA (North of Panhandle) - carved from Western Addition
    nopa_coords = [
        (-122.440, 37.778),
        (-122.430, 37.778),
        (-122.430, 37.772),
        (-122.440, 37.772),
        (-122.440, 37.778)
    ]
    new_neighborhoods.append({
        'name': 'NOPA',
        'geometry': Polygon(nopa_coords)
    })
    print("  ✓ Added NOPA")

    # Japantown - carved from Western Addition
    japantown_coords = [
        (-122.433, 37.788),
        (-122.428, 37.788),
        (-122.428, 37.783),
        (-122.433, 37.783),
        (-122.433, 37.788)
    ]
    new_neighborhoods.append({
        'name': 'Japantown',
        'geometry': Polygon(japantown_coords)
    })
    print("  ✓ Added Japantown")

    # Cole Valley - between Haight Ashbury and Inner Sunset
    cole_valley_coords = [
        (-122.453, 37.768),
        (-122.448, 37.768),
        (-122.448, 37.763),
        (-122.453, 37.763),
        (-122.453, 37.768)
    ]
    new_neighborhoods.append({
        'name': 'Cole Valley',
        'geometry': Polygon(cole_valley_coords)
    })
    print("  ✓ Added Cole Valley")

    # Lower Haight - carved from Haight Ashbury (eastern part)
    lower_haight_coords = [
        (-122.433, 37.773),
        (-122.425, 37.773),
        (-122.425, 37.768),
        (-122.433, 37.768),
        (-122.433, 37.773)
    ]
    new_neighborhoods.append({
        'name': 'Lower Haight',
        'geometry': Polygon(lower_haight_coords)
    })
    print("  ✓ Added Lower Haight")

    # Alamo Square - small area in Western Addition
    alamo_square_coords = [
        (-122.438, 37.778),
        (-122.433, 37.778),
        (-122.433, 37.773),
        (-122.438, 37.773),
        (-122.438, 37.778)
    ]
    new_neighborhoods.append({
        'name': 'Alamo Square',
        'geometry': Polygon(alamo_square_coords)
    })
    print("  ✓ Added Alamo Square")

    # Fillmore - in Western Addition
    fillmore_coords = [
        (-122.438, 37.788),
        (-122.428, 37.788),
        (-122.428, 37.778),
        (-122.438, 37.778),
        (-122.438, 37.788)
    ]
    new_neighborhoods.append({
        'name': 'Fillmore',
        'geometry': Polygon(fillmore_coords)
    })
    print("  ✓ Added Fillmore")

    # Create new GeoDataFrame with added neighborhoods
    new_gdf = gpd.GeoDataFrame(new_neighborhoods, crs=gdf.crs)

    # Combine with existing
    combined_gdf = gpd.GeoDataFrame(
        pd.concat([gdf[['name', 'geometry']], new_gdf], ignore_index=True),
        crs=gdf.crs
    )

    return combined_gdf

def curate_neighborhoods(gdf):
    """Keep only the most essential/commonly discussed neighborhoods."""
    print("\nCurating neighborhood list...")

    # Neighborhoods to keep (essential ones)
    keep_list = [
        # Tier 1 - Core SF
        'Financial District', 'South of Market', 'Mission', 'Mission Bay',
        'Castro/Upper Market', 'Haight Ashbury', 'Marina', 'North Beach',
        'Chinatown', 'Tenderloin', 'Nob Hill', 'Russian Hill',
        'Pacific Heights', 'Hayes Valley', 'Dogpatch', 'Potrero Hill',
        # Tier 2 - Frequently discussed
        'NOPA', 'Inner Richmond', 'Outer Richmond', 'Inner Sunset', 'Outer Sunset',
        'Japantown', 'Western Addition', 'Presidio', 'Bernal Heights',
        'Noe Valley', 'Cole Valley', 'Lower Haight',
        # Tier 3 - Bonus
        'Glen Park', 'Twin Peaks', 'Alamo Square', 'Fillmore', 'Bayview',
        'Downtown/Civic Center', 'Presidio Heights', 'Seacliff',
        'Golden Gate Park', 'Treasure Island/YBI'
    ]

    # Filter to keep only these
    curated = gdf[gdf['name'].isin(keep_list)].copy()

    # Rename some for clarity
    curated.loc[curated['name'] == 'Castro/Upper Market', 'name'] = 'Castro'
    curated.loc[curated['name'] == 'South of Market', 'name'] = 'SoMa'
    curated.loc[curated['name'] == 'Downtown/Civic Center', 'name'] = 'Downtown'

    print(f"  Kept {len(curated)} essential neighborhoods")
    return curated

def create_neighborhood_map(gdf, neighborhood_name, output_path):
    """Create a map image with one neighborhood highlighted."""
    fig, ax = plt.subplots(figsize=(10, 12))

    # Reproject to Web Mercator for basemap
    gdf_projected = gdf.to_crs(epsg=3857)

    # Find the specific neighborhood
    target = gdf_projected[gdf_projected['name'] == neighborhood_name]

    if len(target) == 0:
        print(f"Warning: Neighborhood '{neighborhood_name}' not found")
        return False

    # Plot all neighborhoods in light gray
    gdf_projected.boundary.plot(ax=ax, linewidth=1, edgecolor='gray', alpha=0.5)
    gdf_projected.plot(ax=ax, color='lightgray', alpha=0.3)

    # Highlight the target neighborhood
    target.plot(ax=ax, color='#FF4444', alpha=0.7, edgecolor='darkred', linewidth=2)

    # Try to add basemap (will fail silently if no connection)
    try:
        ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron, zoom=12)
    except:
        pass

    # Remove axis labels
    ax.set_axis_off()

    # Add title
    plt.title("Which San Francisco neighborhood is highlighted?",
              fontsize=16, fontweight='bold', pad=20)

    # Save
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

    return True

def generate_deck():
    """Generate the comprehensive Anki deck."""

    # Download base data
    gdf = download_base_neighborhoods()

    # Add missing neighborhoods
    gdf = add_missing_neighborhoods(gdf)

    # Curate to essential ones
    gdf = curate_neighborhoods(gdf)

    print(f"\nFinal neighborhood list ({len(gdf)} total):")
    for idx, name in enumerate(sorted(gdf['name'].unique()), 1):
        print(f"  {idx:2d}. {name}")

    # Create images directory
    os.makedirs('images_comprehensive', exist_ok=True)

    # Create model
    neighborhood_model = genanki.Model(
        1607392321,
        'SF Neighborhood Model (Comprehensive)',
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
        2059400112,
        'San Francisco Neighborhoods (Comprehensive)'
    )

    media_files = []

    # Generate maps
    print("\nGenerating maps...")
    for neighborhood in sorted(gdf['name'].unique()):
        filename = f"{neighborhood.replace(' ', '_').replace('/', '-').lower()}.png"
        filepath = os.path.join('images_comprehensive', filename)

        print(f"  Creating map for {neighborhood}...")
        success = create_neighborhood_map(gdf, neighborhood, filepath)

        if success:
            media_files.append(filepath)

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
    package.write_to_file('sf_neighborhoods_comprehensive.apkg')

    print(f"\n✓ Created comprehensive deck with {len(media_files)} neighborhoods")
    print(f"✓ Deck saved as: sf_neighborhoods_comprehensive.apkg")

if __name__ == '__main__':
    generate_deck()
