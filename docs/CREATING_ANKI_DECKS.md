# Instructions for AI: Creating Anki Decks

**Audience:** This document is for future AI instances generating Anki decks programmatically.

**Purpose:** Step-by-step instructions to create `.apkg` files that work correctly in Anki.

## Critical Requirements Checklist

Before you start, verify:
- [ ] Python 3 is available
- [ ] You can install packages with pip
- [ ] You have write access to create files and directories
- [ ] You understand the user's requirements for the deck

## Step-by-Step Process

### Step 1: Install Required Library

```bash
pip install genanki
```

**Also install if working with images:**
```bash
pip install pillow
```

**Also install if working with geographic data:**
```bash
pip install geopandas matplotlib contextily shapely
```

### Step 2: Create Your Python Script

Start with this template structure:

```python
#!/usr/bin/env python3
import genanki
import os

def generate_deck():
    # Step 2a: Define the model
    model = create_model()

    # Step 2b: Create the deck
    deck = create_deck()

    # Step 2c: Generate content and add notes
    media_files = []
    items = get_items_to_study()  # Your data source

    for item in items:
        note = create_note(model, item)
        deck.add_note(note)

        # If you have media, track the files
        if item.has_media:
            media_files.append(item.media_path)

    # Step 2d: Package and export
    package = genanki.Package(deck)
    package.media_files = media_files
    package.write_to_file('output.apkg')

    print(f"✓ Created deck with {len(items)} cards")

if __name__ == '__main__':
    generate_deck()
```

### Step 3: Define Your Model (Card Template)

The model defines how cards look. **CRITICAL**: The field names in your model MUST match what you use later.

```python
def create_model():
    return genanki.Model(
        1607392321,  # ⚠️ Use a unique random 10-digit number
        'Your Model Name',
        fields=[
            {'name': 'Front'},   # ⚠️ Remember these exact names
            {'name': 'Back'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Front}}',  # ⚠️ Must match field name exactly
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
            }
        '''
    )
```

**Common Mistakes:**
- ❌ Typo in field name: `fields=[{'name': 'Frnt'}]` then using `{{Front}}`
- ❌ Case mismatch: `fields=[{'name': 'front'}]` then using `{{Front}}`
- ❌ Reusing model ID from another deck

### Step 4: Create the Deck

```python
def create_deck():
    return genanki.Deck(
        2059400112,  # ⚠️ Use a unique random 10-digit number (different from model ID)
        'Your Deck Name'
    )
```

### Step 5: Create Notes (Individual Cards)

**WITHOUT media:**

```python
note = genanki.Note(
    model=model,
    fields=[
        'Question text here',  # First field (matches 'Front')
        'Answer text here',    # Second field (matches 'Back')
    ]
)
deck.add_note(note)
```

**WITH images/media:**

```python
# ⚠️ CRITICAL: File must exist BEFORE you create the note
image_filename = 'my_image.png'
image_full_path = f'images/{image_filename}'

# Verify file exists
assert os.path.exists(image_full_path), f"File not found: {image_full_path}"

note = genanki.Note(
    model=model,
    fields=[
        f'<img src="{image_filename}">',  # ⚠️ Use ONLY filename, not path
        'Answer text',
    ]
)
deck.add_note(note)
media_files.append(image_full_path)  # ⚠️ Use FULL path here
```

**KEY RULES FOR MEDIA:**
1. In HTML (`<img src="">`): Use **filename only** → `my_image.png`
2. In `media_files` list: Use **full path** → `images/my_image.png`
3. File must exist before adding to package
4. Every file referenced in HTML must be in `media_files` list

### Step 6: Package and Export

**If you have NO media files:**

```python
deck.write_to_file('my_deck.apkg')
```

**If you have media files (most common):**

```python
package = genanki.Package(deck)
package.media_files = media_files  # ⚠️ List of full paths
package.write_to_file('my_deck.apkg')
```

**Common Mistakes:**
- ❌ Adding same file to `media_files` twice
- ❌ Using relative path in `<img>`: `<img src="images/file.png">` (wrong)
- ❌ Using filename in `media_files`: `media_files.append('file.png')` (wrong)
- ❌ File doesn't exist at path specified

### Step 7: Verify Success

After generation, check:

```python
# Check file was created
assert os.path.exists('my_deck.apkg'), "Deck file not created!"

# Check file size is reasonable
size_mb = os.path.getsize('my_deck.apkg') / (1024 * 1024)
print(f"Deck size: {size_mb:.1f} MB")

# Verify all media files exist
for f in media_files:
    assert os.path.exists(f), f"Missing: {f}"
```

## Complete Working Example

Here's a minimal working example you can test:

```python
#!/usr/bin/env python3
import genanki
import os

# Define model
model = genanki.Model(
    1234567890,
    'Simple Q&A',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[{
        'name': 'Card',
        'qfmt': '{{Question}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    }],
    css='.card { font-family: arial; text-align: center; }'
)

# Create deck
deck = genanki.Deck(9876543210, 'Test Deck')

# Add cards
cards = [
    ('What is 2+2?', '4'),
    ('What is the capital of France?', 'Paris'),
    ('What is H2O?', 'Water'),
]

for question, answer in cards:
    note = genanki.Note(model=model, fields=[question, answer])
    deck.add_note(note)

# Export
deck.write_to_file('test_deck.apkg')
print(f"✓ Created deck with {len(cards)} cards")
```

## Common Failure Modes and Solutions

### Problem: "Cards appear blank in Anki"

**Cause:** Field name mismatch between model definition and template.

**Debug:**
1. Check your model's `fields` list: `[{'name': 'Question'}, ...]`
2. Check your template: `'qfmt': '{{Question}}'`
3. These MUST match exactly (case-sensitive)

**Solution:**
```python
# ✓ Correct
fields=[{'name': 'Question'}]
qfmt='{{Question}}'

# ✗ Wrong (case mismatch)
fields=[{'name': 'question'}]
qfmt='{{Question}}'
```

### Problem: "Images don't show up in Anki"

**Cause:** Media file path mismatch or file doesn't exist.

**Debug checklist:**
1. Does the file exist? `os.path.exists(full_path)`
2. Is the full path in `media_files`? → `'images/file.png'`
3. Is only the filename in HTML? → `'<img src="file.png">'`
4. Are all referenced files in the `media_files` list?

**Solution:**
```python
# ✓ Correct
image_path = 'my_images/neighborhood.png'
media_files.append(image_path)  # Full path
fields=[f'<img src="neighborhood.png">']  # Filename only

# ✗ Wrong
media_files.append('neighborhood.png')  # Missing directory
fields=[f'<img src="my_images/neighborhood.png">']  # Has path
```

### Problem: "Script runs but .apkg file is tiny/corrupted"

**Cause:** No notes were added to deck, or package creation failed.

**Debug:**
```python
print(f"Notes in deck: {len(deck.notes)}")
print(f"Media files: {len(media_files)}")
```

**Solution:** Ensure you're calling `deck.add_note(note)` for each card.

### Problem: "Can't import deck - duplicate ID error"

**Cause:** Model ID or Deck ID conflicts with existing deck.

**Solution:** Use different random 10-digit numbers for IDs.

## Special Case: Dynamic Image Generation

If you're generating images (like maps) instead of using pre-existing ones:

```python
import matplotlib.pyplot as plt

def create_image(data, output_path):
    """Generate an image and save it."""
    fig, ax = plt.subplots(figsize=(10, 12))

    # Your plotting code here
    # ...

    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()  # ⚠️ Important: close figure to free memory

# Then use it:
os.makedirs('images', exist_ok=True)  # Create directory first

for item in items:
    image_path = f'images/{item.name}.png'
    create_image(item, image_path)  # Generate image

    # Verify it was created
    assert os.path.exists(image_path), f"Failed to create {image_path}"

    media_files.append(image_path)
    note = genanki.Note(model=model, fields=[
        f'<img src="{item.name}.png">',
        item.answer
    ])
    deck.add_note(note)
```

## Execution Order Summary

**DO THIS IN ORDER:**

1. Install dependencies (`pip install genanki`)
2. Create directory for images if needed (`os.makedirs()`)
3. Generate/prepare all media files
4. Define model (with correct field names)
5. Create deck
6. Loop through your data:
   - Verify media file exists
   - Create note with correct field order
   - Add note to deck
   - Add media file path to `media_files` list
7. Create package with media_files list
8. Write to .apkg file
9. Verify output file exists and has reasonable size

**DO NOT:**
- Skip verifying files exist
- Mix up filename vs full path
- Create notes before images exist
- Forget to close matplotlib figures (memory leak)
- Use the same ID for multiple decks

## Testing Your Deck

Before considering it done:

1. **Check file was created:**
   ```python
   assert os.path.exists('deck.apkg')
   ```

2. **Check file size is reasonable:**
   ```python
   size_mb = os.path.getsize('deck.apkg') / (1024 * 1024)
   print(f"Deck size: {size_mb:.1f} MB")
   # Should be >1KB, probably many MB if you have images
   ```

3. **Count should match expectations:**
   ```python
   print(f"Created {len(deck.notes)} cards")
   print(f"With {len(media_files)} media files")
   ```

4. **Tell the user:** "Created deck with X cards, Y MB"

## Example Output Messages

When successful, print clear confirmation:

```python
print(f"✓ Created deck with {len(neighborhoods)} neighborhoods")
print(f"✓ Generated {len(media_files)} map images")
print(f"✓ Deck saved as: sf_neighborhoods.apkg")
```

## Reference Implementations

See these files for working examples:
- `generate_deck_comprehensive.py` - Full geographic deck with 38 cards
- `generate_deck_real_maps.py` - Using GeoJSON and matplotlib
- `generate_deck.py` - Simple SVG-based version

## Key Takeaways for AI Instances

1. **Fields must match exactly** - Most common error
2. **Media requires two paths** - filename in HTML, full path in list
3. **Verify files exist** - Before adding to package
4. **Close matplotlib figures** - Prevent memory leaks
5. **Use unique IDs** - Random 10-digit numbers
6. **Test the output** - Check file exists and size is reasonable
7. **Print clear status** - User needs to know it worked

## When You Get Stuck

If deck creation is failing:

1. Start with the minimal example (no images)
2. Verify that works
3. Add ONE image manually
4. Verify that works
5. Then scale up to full generation

If user reports "doesn't work in Anki":
- Ask them to check: File size, number of cards shown, whether images appear
- Most likely: field name mismatch or media path issue
- Have them try the minimal example deck first
