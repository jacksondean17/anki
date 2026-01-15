# San Francisco Neighborhoods Anki Deck

An Anki flashcard deck to help you learn San Francisco neighborhoods through visual location recognition.

## 🎯 Recommended Deck

**`sf_neighborhoods_real.apkg`** - **37 neighborhoods** with real geographic boundaries

This deck uses actual San Francisco neighborhood boundary data to create accurate maps showing the true shape and location of each neighborhood.

### What's Included

**37 San Francisco neighborhoods** including:

- Bayview, Bernal Heights, Castro/Upper Market, Chinatown
- Crocker Amazon, Diamond Heights, Downtown/Civic Center, Excelsior
- Financial District, Glen Park, Golden Gate Park, Haight Ashbury
- Inner Richmond, Inner Sunset, Lakeshore, Marina
- Mission, Nob Hill, Noe Valley, North Beach
- Ocean View, Outer Mission, Outer Richmond, Outer Sunset
- Pacific Heights, Parkside, Potrero Hill, Presidio, Presidio Heights
- Russian Hill, Seacliff, South of Market, Treasure Island/YBI
- Twin Peaks, Visitacion Valley, West of Twin Peaks, Western Addition

## How It Works

Each flashcard shows:
- **Front**: A map of San Francisco with one neighborhood highlighted in red
- **Back**: The name of the highlighted neighborhood

The maps show actual neighborhood boundaries from open data sources, with all neighborhoods outlined for geographic context.

## Installation

1. Download `sf_neighborhoods_real.apkg` from this repository (7.9 MB)
2. Open Anki on your computer or mobile device
3. Click "File" → "Import" (or use the import button)
4. Select the `.apkg` file
5. Start studying!

## Regenerating the Deck

To regenerate the deck with real maps:

```bash
# Install dependencies
pip install -r requirements.txt

# Generate the deck
python3 generate_deck_real_maps.py
```

This will:
1. Download neighborhood boundary data from Code for America's open data
2. Generate map images for each neighborhood
3. Create the Anki deck file

## Alternative: Simple SVG Deck

**`sf_neighborhoods.apkg`** - Simplified version with 14 neighborhoods using basic SVG graphics

For a lighter deck with simplified maps, use `generate_deck.py` instead.

## Files

- `sf_neighborhoods_real.apkg` - Main Anki deck with real maps (recommended)
- `sf_neighborhoods.apkg` - Simplified Anki deck with SVG graphics
- `generate_deck_real_maps.py` - Script to generate deck with real maps
- `generate_deck.py` - Script to generate simplified deck
- `requirements.txt` - Python dependencies
- `images_real/` - PNG images with real neighborhood boundaries
- `images/` - SVG images (simplified graphics)
- `sf_neighborhoods.geojson` - Neighborhood boundary data

## Data Sources

Neighborhood boundary data sourced from:
- [Code for America Click That Hood](https://github.com/codeforamerica/click_that_hood) - Open neighborhood boundary data
