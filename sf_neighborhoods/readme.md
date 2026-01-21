# San Francisco Neighborhoods Anki Deck

An Anki flashcard deck to help you learn San Francisco neighborhoods through visual location recognition.

## 🎯 Recommended Deck

**`sf_neighborhoods_comprehensive.apkg`** - **38 essential neighborhoods** (7.0 MB)

This is the most complete deck with all the neighborhoods you need to know for fluency in SF discussions. Includes popular neighborhoods like Mission Bay, Dogpatch, Hayes Valley, Tenderloin, NOPA, Japantown, and more that were missing from other datasets.

### What's Included

**38 essential San Francisco neighborhoods:**

**Core SF (16):** Financial District, SoMa, Mission, Mission Bay, Castro, Haight Ashbury, Marina, North Beach, Chinatown, Tenderloin, Nob Hill, Russian Hill, Pacific Heights, Hayes Valley, Dogpatch, Potrero Hill

**Frequently Discussed (12):** NOPA, Inner Richmond, Outer Richmond, Inner Sunset, Outer Sunset, Japantown, Western Addition, Presidio, Bernal Heights, Noe Valley, Cole Valley, Lower Haight

**Bonus Neighborhoods (10):** Glen Park, Twin Peaks, Alamo Square, Fillmore, Bayview, Downtown, Presidio Heights, Seacliff, Golden Gate Park, Treasure Island/YBI

## How It Works

Each flashcard shows:
- **Front**: A map of San Francisco with one neighborhood highlighted in red
- **Back**: The name of the highlighted neighborhood

The maps show actual neighborhood boundaries from open data sources, with all neighborhoods outlined for geographic context.

## Installation

1. Download `sf_neighborhoods_comprehensive.apkg` from this repository (7.0 MB)
2. Open Anki on your computer or mobile device
3. Click "File" → "Import" (or use the import button)
4. Select the `.apkg` file
5. Start studying!

## Regenerating the Deck

To regenerate the comprehensive deck:

```bash
# Install dependencies
pip install -r requirements.txt

# Generate the comprehensive deck
python3 generate_deck_comprehensive.py
```

This will:
1. Download base neighborhood boundary data from Code for America
2. Add 10 key neighborhoods that are commonly discussed but missing from official datasets (Mission Bay, Dogpatch, Hayes Valley, Tenderloin, NOPA, Japantown, Cole Valley, Lower Haight, Alamo Square, Fillmore)
3. Generate map images for all 38 neighborhoods
4. Create the Anki deck file

## Alternative Versions

**`sf_neighborhoods_real.apkg`** (7.9 MB) - 37 neighborhoods from official open data sources only
- Use `python3 generate_deck_real_maps.py` to regenerate

**`sf_neighborhoods.apkg`** (71 KB) - 14 neighborhoods with simplified SVG graphics
- Use `python3 generate_deck.py` to regenerate

## Files

- `sf_neighborhoods_comprehensive.apkg` - **Comprehensive deck with 38 neighborhoods (recommended)**
- `sf_neighborhoods_real.apkg` - Deck with 37 official neighborhoods
- `sf_neighborhoods.apkg` - Simplified deck with 14 neighborhoods (SVG graphics)
- `generate_deck_comprehensive.py` - Script to generate comprehensive deck
- `generate_deck_real_maps.py` - Script to generate official neighborhoods deck
- `generate_deck.py` - Script to generate simplified deck
- `requirements.txt` - Python dependencies
- `images_comprehensive/` - PNG images for comprehensive deck (38 neighborhoods)
- `images_real/` - PNG images for official neighborhoods (37 neighborhoods)
- `images/` - SVG images for simplified deck (14 neighborhoods)
- `sf_neighborhoods_base.geojson` - Base neighborhood boundary data

## Data Sources

Neighborhood boundary data sourced from:
- [Code for America Click That Hood](https://github.com/codeforamerica/click_that_hood) - Open neighborhood boundary data
- Manual additions for 10 commonly-discussed neighborhoods (Mission Bay, Dogpatch, Hayes Valley, Tenderloin, NOPA, Japantown, Cole Valley, Lower Haight, Alamo Square, Fillmore)
