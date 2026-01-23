#!/usr/bin/env python3
import genanki
import os
from PIL import Image, ImageDraw, ImageFont

def create_card_image(rank, suit, x, y, draw, card_width=100, card_height=140):
    """Draw a single playing card at position (x, y)."""
    # Card background (white)
    draw.rectangle([x, y, x + card_width, y + card_height], fill='white', outline='black', width=2)

    # Suit symbols and colors
    suit_symbols = {'♠': 'black', '♥': 'red', '♦': 'red', '♣': 'black'}
    color = suit_symbols.get(suit, 'black')

    # Try to use a larger font, fall back to default if not available
    try:
        font_rank = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
        font_suit = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
    except:
        font_rank = ImageFont.load_default()
        font_suit = ImageFont.load_default()

    # Draw rank in top-left
    draw.text((x + 10, y + 5), rank, fill=color, font=font_rank)

    # Draw suit symbol in center
    draw.text((x + card_width//2 - 15, y + card_height//2 - 20), suit, fill=color, font=font_suit)

    # Draw rank in bottom-right (upside down effect)
    draw.text((x + card_width - 30, y + card_height - 40), rank, fill=color, font=font_rank)

def create_poker_hand_image(hand_name, cards, output_path):
    """Create an image showing a poker hand.

    Args:
        hand_name: Name of the poker hand (not displayed on image)
        cards: List of tuples (rank, suit) for each card
        output_path: Where to save the image
    """
    # Image dimensions
    card_width = 100
    card_height = 140
    card_spacing = 20
    padding = 40

    img_width = padding * 2 + card_width * 5 + card_spacing * 4
    img_height = padding * 2 + card_height

    # Create image
    img = Image.new('RGB', (img_width, img_height), color='#2d5016')  # Poker table green
    draw = ImageDraw.Draw(img)

    # Draw cards (no title)
    y_pos = padding
    for i, (rank, suit) in enumerate(cards):
        x_pos = padding + i * (card_width + card_spacing)
        create_card_image(rank, suit, x_pos, y_pos, draw, card_width, card_height)

    img.save(output_path)
    print(f"  Created: {output_path}")

def get_poker_hands():
    """Define all poker hands from lowest to highest with example cards and probabilities."""
    hands = [
        {
            'name': 'Royal Flush',
            'rank': 10,
            'cards': [('A', '♠'), ('K', '♠'), ('Q', '♠'), ('J', '♠'), ('10', '♠')],
            'description': 'A, K, Q, J, 10 of the same suit',
            'probability': '0.00015%',
            'odds': '1 in 649,740',
            'holdem_probability': '0.0032%',
            'holdem_odds': '1 in 30,940'
        },
        {
            'name': 'Straight Flush',
            'rank': 9,
            'cards': [('9', '♥'), ('8', '♥'), ('7', '♥'), ('6', '♥'), ('5', '♥')],
            'description': 'Five consecutive cards of the same suit',
            'probability': '0.00139%',
            'odds': '1 in 72,193',
            'holdem_probability': '0.0279%',
            'holdem_odds': '1 in 3,590'
        },
        {
            'name': 'Four of a Kind',
            'rank': 8,
            'cards': [('K', '♠'), ('K', '♥'), ('K', '♦'), ('K', '♣'), ('3', '♠')],
            'description': 'Four cards of the same rank',
            'probability': '0.0240%',
            'odds': '1 in 4,165',
            'holdem_probability': '0.168%',
            'holdem_odds': '1 in 595'
        },
        {
            'name': 'Full House',
            'rank': 7,
            'cards': [('J', '♠'), ('J', '♥'), ('J', '♦'), ('8', '♣'), ('8', '♠')],
            'description': 'Three of a kind plus a pair',
            'probability': '0.144%',
            'odds': '1 in 694',
            'holdem_probability': '2.60%',
            'holdem_odds': '1 in 38'
        },
        {
            'name': 'Flush',
            'rank': 6,
            'cards': [('K', '♦'), ('J', '♦'), ('9', '♦'), ('6', '♦'), ('3', '♦')],
            'description': 'Five cards of the same suit',
            'probability': '0.197%',
            'odds': '1 in 509',
            'holdem_probability': '3.03%',
            'holdem_odds': '1 in 33'
        },
        {
            'name': 'Straight',
            'rank': 5,
            'cards': [('10', '♠'), ('9', '♥'), ('8', '♦'), ('7', '♣'), ('6', '♠')],
            'description': 'Five consecutive cards of different suits',
            'probability': '0.392%',
            'odds': '1 in 255',
            'holdem_probability': '4.62%',
            'holdem_odds': '1 in 22'
        },
        {
            'name': 'Three of a Kind',
            'rank': 4,
            'cards': [('7', '♠'), ('7', '♥'), ('7', '♦'), ('K', '♣'), ('2', '♠')],
            'description': 'Three cards of the same rank',
            'probability': '2.11%',
            'odds': '1 in 47',
            'holdem_probability': '4.83%',
            'holdem_odds': '1 in 21'
        },
        {
            'name': 'Two Pair',
            'rank': 3,
            'cards': [('J', '♠'), ('J', '♥'), ('5', '♦'), ('5', '♣'), ('2', '♠')],
            'description': 'Two different pairs',
            'probability': '4.75%',
            'odds': '1 in 21',
            'holdem_probability': '23.5%',
            'holdem_odds': '1 in 4.3'
        },
        {
            'name': 'One Pair',
            'rank': 2,
            'cards': [('10', '♠'), ('10', '♥'), ('K', '♦'), ('7', '♣'), ('3', '♠')],
            'description': 'Two cards of the same rank',
            'probability': '42.3%',
            'odds': '1 in 2.4',
            'holdem_probability': '43.8%',
            'holdem_odds': '1 in 2.3'
        },
        {
            'name': 'High Card',
            'rank': 1,
            'cards': [('A', '♠'), ('J', '♥'), ('8', '♦'), ('5', '♣'), ('2', '♠')],
            'description': 'No matching cards',
            'probability': '50.1%',
            'odds': '1 in 2.0',
            'holdem_probability': '17.4%',
            'holdem_odds': '1 in 5.7'
        },
    ]

    return sorted(hands, key=lambda x: x['rank'])

def create_model():
    """Create the Anki card model with Front/Back fields."""
    return genanki.Model(
        1592638471,  # Unique random 10-digit number
        'Poker Hand Ranking',
        fields=[
            {'name': 'Front'},
            {'name': 'Back'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Front}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Back}}',
            },
        ],
        css='''
            .card {
                font-family: arial;
                font-size: 20px;
                text-align: center;
                color: black;
                background-color: white;
                padding: 20px;
            }
            img {
                max-width: 100%;
                height: auto;
                display: block;
                margin: 0 auto;
            }
            .back {
                text-align: center;
                font-size: 22px;
                line-height: 1.6;
            }
            .beats {
                color: #2d8c2d;
                font-weight: bold;
            }
            .loses {
                color: #cc3333;
                font-weight: bold;
            }
        '''
    )

def create_deck():
    """Create the Anki deck."""
    return genanki.Deck(
        2847291638,  # Unique random 10-digit number
        'Poker Hand Rankings'
    )

def generate_deck():
    """Main function to generate the Anki deck."""
    print("Generating Poker Hands Anki deck...")

    # Create images directory
    images_dir = 'images'
    os.makedirs(images_dir, exist_ok=True)

    # Get poker hands
    hands = get_poker_hands()

    # Generate images for each hand
    print("\nGenerating hand images...")
    media_files = []

    for hand in hands:
        filename = f"{hand['name'].lower().replace(' ', '_')}.png"
        filepath = os.path.join(images_dir, filename)
        create_poker_hand_image(hand['name'], hand['cards'], filepath)
        hand['image_filename'] = filename
        hand['image_filepath'] = filepath
        media_files.append(filepath)

    # Create model and deck
    model = create_model()
    deck = create_deck()

    # Create notes
    print("\nCreating flashcards...")
    for i, hand in enumerate(hands):
        # Determine what beats and loses to this hand
        beats = hands[i-1]['name'] if i > 0 else "Nothing"
        loses_to = hands[i+1]['name'] if i < len(hands)-1 else "Nothing"

        # Front: image of the hand (no label)
        front = f'<img src="{hand["image_filename"]}">'

        # Back: what it is, what it beats/loses to, and probability
        back = f'''<div class="back">
<p><strong>{hand['name']}</strong></p>
<p style="font-size: 16px; color: #666;">{hand['description']}</p>
<hr>
<p class="beats">Beats: {beats}</p>
<p class="loses">Loses to: {loses_to}</p>
<hr>
<p style="font-size: 16px; color: #444;"><strong>Texas Hold'em Odds:</strong> {hand['holdem_odds']}</p>
<p style="font-size: 14px; color: #888;">({hand['holdem_probability']} of all 7-card hands)</p>
</div>'''

        # Verify image exists
        assert os.path.exists(hand['image_filepath']), f"Image not found: {hand['image_filepath']}"

        note = genanki.Note(
            model=model,
            fields=[front, back]
        )
        deck.add_note(note)
        print(f"  Added card: {hand['name']}")

    # Package and export
    print("\nPackaging deck...")
    package = genanki.Package(deck)
    package.media_files = media_files

    output_path = 'poker_hands.apkg'
    package.write_to_file(output_path)

    # Verify and report
    assert os.path.exists(output_path), "Deck file not created!"
    size_mb = os.path.getsize(output_path) / (1024 * 1024)

    print(f"\n✓ Created deck with {len(hands)} cards")
    print(f"✓ Generated {len(media_files)} hand images")
    print(f"✓ Deck saved as: {output_path}")
    print(f"✓ File size: {size_mb:.2f} MB")

if __name__ == '__main__':
    generate_deck()
