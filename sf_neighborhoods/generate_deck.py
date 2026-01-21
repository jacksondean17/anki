#!/usr/bin/env python3
"""
Generate an Anki deck for San Francisco neighborhoods.
Each card shows a map with a highlighted neighborhood on the front,
and the neighborhood name on the back.
"""

import genanki
import os
import random

# Create a model for the neighborhood cards
neighborhood_model = genanki.Model(
    1607392319,  # Random model ID
    'SF Neighborhood Model',
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
            max-width: 90%;
            max-height: 400px;
        }
    """
)

# San Francisco neighborhoods with their approximate positions
neighborhoods = [
    ("Mission District", "#FF6B6B", "M 300 380 L 340 380 L 340 450 L 300 450 Z"),
    ("Castro", "#4ECDC4", "M 260 360 L 300 360 L 300 410 L 260 410 Z"),
    ("Haight-Ashbury", "#45B7D1", "M 220 320 L 270 320 L 270 360 L 220 360 Z"),
    ("Marina District", "#96CEB4", "M 220 180 L 300 180 L 300 220 L 220 220 Z"),
    ("North Beach", "#FFEAA7", "M 320 220 L 360 220 L 360 260 L 320 260 Z"),
    ("Chinatown", "#DFE6E9", "M 300 240 L 340 240 L 340 280 L 300 280 Z"),
    ("Financial District", "#A29BFE", "M 340 260 L 380 260 L 380 310 L 340 310 Z"),
    ("SoMa", "#FD79A8", "M 320 310 L 380 310 L 380 370 L 320 370 Z"),
    ("Nob Hill", "#FDCB6E", "M 280 260 L 320 260 L 320 300 L 280 300 Z"),
    ("Russian Hill", "#6C5CE7", "M 260 220 L 300 220 L 300 260 L 260 260 Z"),
    ("Pacific Heights", "#74B9FF", "M 200 240 L 260 240 L 260 290 L 200 290 Z"),
    ("Richmond District", "#A8E6CF", "M 120 200 L 220 200 L 220 280 L 120 280 Z"),
    ("Sunset District", "#FFB6B9", "M 120 320 L 240 320 L 240 420 L 120 420 Z"),
    ("Presidio", "#55E6C1", "M 140 120 L 220 120 L 220 200 L 140 200 Z"),
]

def create_svg_image(neighborhood_name, color, path_data):
    """Create an SVG image with the neighborhood highlighted."""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="500" height="600" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="500" height="600" fill="#f0f0f0"/>

  <!-- Water (San Francisco Bay) -->
  <rect x="0" y="0" width="500" height="120" fill="#a8d8ea"/>
  <rect x="380" y="120" width="120" height="300" fill="#a8d8ea"/>

  <!-- SF Peninsula outline (simplified) -->
  <path d="M 100 120 L 400 120 L 400 180 L 420 200 L 420 450 L 400 480 L 350 500 L 250 520 L 150 500 L 100 450 Z"
        fill="#d0d0d0" stroke="#808080" stroke-width="2"/>

  <!-- Grid for reference -->
  <line x1="120" y1="120" x2="120" y2="520" stroke="#999" stroke-width="0.5" opacity="0.3"/>
  <line x1="220" y1="120" x2="220" y2="520" stroke="#999" stroke-width="0.5" opacity="0.3"/>
  <line x1="320" y1="120" x2="320" y2="520" stroke="#999" stroke-width="0.5" opacity="0.3"/>

  <!-- Highlighted neighborhood -->
  <path d="{path_data}" fill="{color}" opacity="0.8" stroke="#333" stroke-width="3"/>

  <!-- Title -->
  <text x="250" y="570" font-family="Arial, sans-serif" font-size="20"
        fill="#333" text-anchor="middle" font-weight="bold">
    Which San Francisco neighborhood is highlighted?
  </text>
</svg>'''
    return svg

def generate_deck():
    """Generate the Anki deck."""
    # Create deck
    deck = genanki.Deck(
        2059400110,  # Random deck ID
        'San Francisco Neighborhoods'
    )

    # Create images directory
    os.makedirs('images', exist_ok=True)

    media_files = []

    # Create cards for each neighborhood
    for neighborhood_name, color, path_data in neighborhoods:
        # Generate SVG image
        svg_content = create_svg_image(neighborhood_name, color, path_data)

        # Save SVG file
        filename = f"{neighborhood_name.replace(' ', '_').lower()}.svg"
        filepath = os.path.join('images', filename)

        with open(filepath, 'w') as f:
            f.write(svg_content)

        media_files.append(filepath)

        # Create note
        note = genanki.Note(
            model=neighborhood_model,
            fields=[
                f'<img src="{filename}">',
                neighborhood_name
            ]
        )

        deck.add_note(note)

    # Generate package
    package = genanki.Package(deck)
    package.media_files = media_files
    package.write_to_file('sf_neighborhoods.apkg')

    print(f"✓ Created deck with {len(neighborhoods)} neighborhoods")
    print(f"✓ Generated {len(media_files)} images")
    print(f"✓ Deck saved as: sf_neighborhoods.apkg")

if __name__ == '__main__':
    generate_deck()
