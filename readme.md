# San Francisco Neighborhoods Anki Deck

An Anki flashcard deck to help you learn San Francisco neighborhoods through visual location recognition.

## What's Included

This deck contains **14 San Francisco neighborhoods**:

- Castro
- Chinatown
- Financial District
- Haight-Ashbury
- Marina District
- Mission District
- Nob Hill
- North Beach
- Pacific Heights
- Presidio
- Richmond District
- Russian Hill
- SoMa (South of Market)
- Sunset District

## How It Works

Each flashcard shows:
- **Front**: A simplified map of San Francisco with one neighborhood highlighted in color
- **Back**: The name of the highlighted neighborhood

The maps include San Francisco Bay for orientation and show the approximate location of each neighborhood on the peninsula.

## Installation

1. Download `sf_neighborhoods.apkg` from this repository
2. Open Anki on your computer or mobile device
3. Click "File" → "Import" (or use the import button)
4. Select the `sf_neighborhoods.apkg` file
5. Start studying!

## Regenerating the Deck

If you want to modify or regenerate the deck:

```bash
# Install dependencies
pip install -r requirements.txt

# Generate the deck
python3 generate_deck.py
```

This will create:
- `sf_neighborhoods.apkg` - The Anki deck file
- `images/` - Directory containing SVG images for each neighborhood

## Files

- `sf_neighborhoods.apkg` - Ready-to-import Anki deck
- `generate_deck.py` - Python script to generate the deck
- `requirements.txt` - Python dependencies
- `images/` - SVG images for each neighborhood
