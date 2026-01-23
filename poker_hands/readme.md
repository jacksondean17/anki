# Poker Hand Rankings

Learn poker hand rankings through recognition-based flashcards with visual examples and Texas Hold'em probabilities.

## What's Included

**10 cards** covering all standard poker hands from High Card to Royal Flush (133 KB)

## Download

- [Poker Hand Rankings](https://raw.githubusercontent.com/jacksondean17/anki/main/poker_hands/poker_hands.apkg)

## Card Format

**Front Side:**
- Visual representation of 5 playing cards
- **No labels** - pure recognition testing
- Example hand shown with specific cards

**Back Side:**
- **Hand name** and brief description
- **Beats:** The hand immediately below in ranking
- **Loses to:** The hand immediately above in ranking
- **Texas Hold'em Odds:** Probability of making this hand (7 cards total)

## Hand Rankings (Lowest to Highest)

1. **High Card** - No matching cards
2. **One Pair** - Two cards of the same rank
3. **Two Pair** - Two different pairs
4. **Three of a Kind** - Three cards of the same rank
5. **Straight** - Five consecutive cards of different suits
6. **Flush** - Five cards of the same suit
7. **Full House** - Three of a kind plus a pair
8. **Four of a Kind** - Four cards of the same rank
9. **Straight Flush** - Five consecutive cards of the same suit
10. **Royal Flush** - A, K, Q, J, 10 of the same suit

## Learning Approach

This deck combines multiple effective learning methods:

1. **Recognition Testing**: No labels on the front - you must identify the hand yourself
2. **Hierarchy Learning**: Each card shows what hands it beats and loses to
3. **Probability Context**: Texas Hold'em odds help you understand hand rarity and value

## Complementary Study Methods

To further improve your poker skills:

1. **Comparative Analysis**: Compare two hands and determine which wins
2. **Scenario-Based Practice**: Use hole cards + community cards (Texas Hold'em format)
3. **Live Play**: Practice identifying hands during actual games
4. **Hand Equity**: Learn how different hands perform against each other pre-flop

## How to Use

1. Download the .apkg file using the link above
2. Import into Anki or AnkiDroid
3. Study regularly to internalize hand rankings
4. Once comfortable with basic rankings, move to scenario-based practice games

## Regenerating the Deck

If you want to modify the deck:

```bash
cd poker_hands
pip install genanki pillow
python3 generate_deck.py
```

This will regenerate `poker_hands.apkg` with any modifications you've made to the script.

## Tips for Learning

- Start by learning the order from lowest to highest
- Remember key transitions: Straight/Flush/Full House are often confused
- "Full House" beats "Flush" (three + two beats five of same suit)
- Practice identifying hands quickly - speed matters in real games
- Consider the probabilities: rarer hands beat more common ones

---

*Generated: 2026-01-23*
