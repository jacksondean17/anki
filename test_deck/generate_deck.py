#!/usr/bin/env python3
"""Test deck to verify the Anki deck generation process is working."""
import genanki
import os


def create_model():
    return genanki.Model(
        1923847561,
        'Test Deck Q&A',
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
        '''
    )


def create_deck():
    return genanki.Deck(
        3847291023,
        'Test Deck'
    )


def get_cards():
    return [
        ("What is 2 + 2?", "4"),
        ("What is the capital of France?", "Paris"),
        ("What color is the sky on a clear day?", "Blue"),
        ("How many sides does a triangle have?", "3"),
        ("What is H2O commonly known as?", "Water"),
    ]


def main():
    model = create_model()
    deck = create_deck()

    for front, back in get_cards():
        note = genanki.Note(model=model, fields=[front, back])
        deck.add_note(note)

    output_path = os.path.join(os.path.dirname(__file__), 'test_deck.apkg')
    package = genanki.Package(deck)
    package.write_to_file(output_path)

    assert os.path.exists(output_path), "Output file was not created!"
    size = os.path.getsize(output_path)
    print(f"Success! Created {output_path} ({size} bytes, {len(get_cards())} cards)")


if __name__ == '__main__':
    main()
