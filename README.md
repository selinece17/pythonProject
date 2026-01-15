# Crazy 8 Card Game

A text-based implementation of the classic Crazy 8 card game in Python, featuring a two-player gameplay system with standard card game rules.

## Overview

Crazy 8 is a popular card game where players try to be the first to get rid of all their cards by matching either the face or suit of the card on top of the discard pile. The number 8 cards are wild and can be played at any time, allowing the player to choose a new suit.

## Project Structure

The project consists of four main Python files:

- **Card.py** - Defines the Card class representing individual playing cards
- **DeckOfCards.py** - Manages a standard 52-card deck with shuffling and dealing functionality
- **crazy8_player.py** - Implements the CPlayer class for managing player hands and actions
- **crazy8_text.py** - Contains the main game loop and text-based user interface

## Features

- Two-player gameplay
- Standard 52-card deck with shuffle functionality
- Full Crazy 8 rules implementation:
  - Match by face or suit
  - 8s are wild cards that allow suit selection
  - Draw up to 3 cards if you can't play
  - First player to empty their hand wins
- Input validation and error handling
- Turn-based gameplay with clear prompts

## Requirements

- Python 3.x
- PIL (Pillow) library (for card image support, optional)

```bash
pip install Pillow
```

## How to Play

### Starting the Game

Run the main game file:

```bash
python crazy8_text.py
```

### Game Rules

1. Each player starts with 7 cards
2. A starting card is placed face-up on the discard pile
3. Players take turns playing cards that match either:
   - The **face** (number/letter) of the top card, OR
   - The **suit** of the top card
4. **Special Rule - 8s are Wild:**
   - An 8 can be played at any time
   - When you play an 8, you choose the suit that the next player must match
5. If you can't play a card, you can draw up to 3 cards from the deck
6. After drawing, you must attempt to play a card
7. First player to run out of cards wins!

### During Your Turn

You'll see your cards displayed with their index numbers:

```
Player 1 has:
0: A of Clubs
1: 5 of Hearts
2: 8 of Diamonds
...
```

**To play a card:** Enter the index number (0, 1, 2, etc.)

**To draw cards:** Type `hit` and follow the prompts

**When playing an 8:** You'll be prompted to choose a suit (clubs, diamonds, hearts, or spades)

### Input Validation

The game includes robust error handling:
- Invalid index numbers result in losing your turn
- Invalid suit choices when playing an 8 will re-prompt you
- Non-integer inputs are rejected with appropriate messages

## Class Documentation

### Card Class

Represents a single playing card with face, suit, value, and optional image.

**Key Methods:**
- `getFace()` - Returns the card's face (A, 2-10, J, Q, K)
- `getSuit()` - Returns the card's suit (Clubs, Diamonds, Hearts, Spades)
- `getValue()` - Returns numeric value for comparisons
- `getImage()` - Returns the card's image object (if loaded)

### DeckOfCards Class

Manages a standard 52-card deck with dealing and shuffling capabilities.

**Key Methods:**
- `shuffle()` - Randomly shuffles the deck
- `dealCard()` - Returns the next card from the deck
- `cardsRemaining()` - Returns number of undealt cards
- `isEmpty()` - Checks if deck is empty
- `reset()` - Resets deck to top without reshuffling

**Optional:** Supports loading card images from a sprite sheet in the `../img/` directory.

### CPlayer Class

Represents a player with their hand of cards and associated methods.

**Key Methods:**
- `addCard(card)` - Adds a card to the player's hand
- `getCard()` - Displays all cards in the player's hand
- `playCard()` - Removes and returns the first card
- `hasCard()` - Returns True if player has cards
- `cardsRemaining()` - Returns number of cards in hand
- `getSpecificCard(index)` - Returns card at specific index
- `removeCard(card)` - Removes a specific card from hand
- `hasSpecificFace(face)` - Checks if player has a card with given face
- `hasSpecificSuit(suit)` - Checks if player has a card with given suit
- `finding(list)` - Finds a card by face and suit
- `trueCard(value)` - Validates if something is a Card object

## Example Gameplay

```
Player 1 has: 
0: A of Clubs
1: 5 of Hearts
2: 8 of Diamonds
3: K of Spades

The card that the game will start is a 5 of Hearts

==================================================
Player 1 will play!
==================================================
Enter the index of the card you want: 1
THE CARD ON TOP IS 5 of Hearts
Player 1 you now have: 
0: A of Clubs
1: 8 of Diamonds
2: K of Spades

==================================================
Player 2 will NOW PLAY
==================================================
...
```

## Testing

Each class file includes built-in unit tests. Run them individually:

```bash
python crazy8_player.py
python DeckOfCards.py
python Card.py
```

The test suite validates:
- Constructor functionality
- Method return values
- Edge cases (empty hands, invalid inputs)
- Card manipulation operations

