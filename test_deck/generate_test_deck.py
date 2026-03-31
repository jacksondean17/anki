#!/usr/bin/env python3
import genanki
import os

# Define model
model = genanki.Model(
    1357924680,
    'Test Q&A Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[{
        'name': 'Card',
        'qfmt': '{{Question}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    }],
    css='.card { font-family: arial; font-size: 20px; text-align: center; color: black; background-color: white; }'
)

# Create deck
deck = genanki.Deck(2468013579, 'Test Deck')

# Add cards
cards = [
    ('What is 2+2?', '4'),
    ('What is the capital of France?', 'Paris'),
    ('What is H2O?', 'Water'),
    ('What color is the sky?', 'Blue'),
    ('How many days in a week?', '7'),
]

for question, answer in cards:
    note = genanki.Note(model=model, fields=[question, answer])
    deck.add_note(note)

# Export
output_path = os.path.join(os.path.dirname(__file__), 'test_deck.apkg')
deck.write_to_file(output_path)

# Verify
assert os.path.exists(output_path), "Deck file not created!"
size_kb = os.path.getsize(output_path) / 1024
print(f"Created {len(deck.notes)} cards")
print(f"Deck size: {size_kb:.1f} KB")
print(f"Deck saved as: {output_path}")
