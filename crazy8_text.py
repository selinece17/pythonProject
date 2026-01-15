'''
Created on Mar 14, 2024
THIS PROGRAM HAS THE TEXT BASED GAME OF CRAZY 8.
'''

from Project1.DeckOfCards import DeckOfCards as DC
from Project1.crazy8_player import CPlayer


# This function checks if the argument is an integer or not
def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def playC():
    # The cards
    warDeck = DC()
    warDeck.shuffle()
    
    # Create the two players
    player = CPlayer(name="Gunes")
    player2 = CPlayer(name="Deniz")
    
    # Giving 7 cards to each player
    for _ in range(7):
        player.addCard(warDeck.dealCard())
        
    for _ in range(7):
        player2.addCard(warDeck.dealCard())
        
    print(f'Player 2 has:')
    player2.getCard()
    print(f'Player 1 has: ')
    player.getCard()
    
    # Using deck_pile to know what the card on top is each time a player is playing
    deck_pile = []
    startCard = warDeck.dealCard()
    deck_pile.append(startCard)
    
    print(f'The card that the game will start is a {startCard}')
    
    # If starting card is an 8, draw another card
    while startCard.getFace() == '8':
        startCard = warDeck.dealCard()
        deck_pile.append(startCard)
        print(f'The starting card was an 8, new starting card is: {startCard}')

    # Suit chosen by player 1 when they play an 8
    chosen_suit_p1 = None
    # Suit chosen by player 2 when they play an 8
    chosen_suit_p2 = None
    
    while player.hasCard() and player2.hasCard():
        suits = ["clubs", "diamonds", "hearts", "spades"]
        
        # player 1's turn
        print('\n' + '='*50)
        print('Player 1 will play!')
        print('='*50)
        
        # Check if previous card was an 8 played by player 2
        if chosen_suit_p2 is not None and deck_pile[-1].getFace() == '8':
            print(f'The previous player chose suit: {chosen_suit_p2}')
            print(f'You must play a card with suit {chosen_suit_p2} or an 8')
            card_num = input("Enter the index of the card you want: ")
            
            # Validate input
            if not is_integer(card_num):
                print('INVALID INPUT! You lost your turn.')
                chosen_suit_p2 = None
                continue
            
            c = player.getSpecificCard(card_num)
            
            if not player.trueCard(c):
                print('WRONG INDEX! You lost your turn.')
                chosen_suit_p2 = None
                continue
            
            # Check if card is valid (either an 8 or matches the chosen suit)
            if c.getFace() == '8':
                # Get valid suit choice
                while True:
                    chosen_suit_p1 = input('What suit do you choose? ').lower()
                    if chosen_suit_p1 in suits:
                        break
                    print(f'Invalid suit! Please choose from: {", ".join(suits)}')
                
                player.removeCard(c)
                deck_pile.append(c)
                print(f'THE CARD ON TOP IS {deck_pile[-1]}')
                print(f'Player 1 you now have: ')
                player.getCard()
                chosen_suit_p2 = None
                
            elif c.getSuit().lower() == chosen_suit_p2.lower():
                player.removeCard(c)
                deck_pile.append(c)
                print(f'THE CARD ON TOP IS {deck_pile[-1]}')
                print(f'Player 1 you now have: ')
                player.getCard()
                chosen_suit_p2 = None  # Reset after use
                chosen_suit_p1 = None  # Clear P1's suit choice
                
            else:
                print('WRONG CARD! You lost your turn, sorry :))))')
                chosen_suit_p2 = None  # Reset after use
        
        else:
            # Normal turn - no 8 suit restriction
            chosen_suit_p2 = None  # Clear any previous 8 suit choice
            
            card_num = input("Enter the index of the card you want or write 'hit' if you want to draw cards: ")
            
            # If player wants to draw cards
            if card_num.lower() == 'hit':
                current = 0
                while current < 3:
                    ask = input("You can pick up to 3 cards! Write 'hit' to get a card and 'done' to stop: ")
                    if ask.lower() == 'hit':
                        current += 1
                        player.addCard(warDeck.dealCard())
                        print(f'Now you have: ')
                        player.getCard()
                    elif ask.lower() == 'done':
                        break
                    else:
                        print("WRONG INPUT - please write 'hit' or 'done'")
                
                # After drawing, player must play a card
                card_num = input("Enter the index of the card you want to play: ")
                
                if not is_integer(card_num):
                    print('INVALID INPUT! You lost your turn.')
                    continue
                
                c = player.getSpecificCard(card_num)
                
            elif is_integer(card_num):
                c = player.getSpecificCard(card_num)
                
            else:
                print('INVALID INPUT! You lost your turn.')
                continue
            
            # Validate the card exists
            if not player.trueCard(c):
                print('WRONG INDEX! You lost your turn.')
                continue
            
            # Check if card is valid to play
            if c.getFace() == '8':
                # Get valid suit choice
                while True:
                    chosen_suit_p1 = input('What suit do you choose? ').lower()
                    if chosen_suit_p1 in suits:
                        break
                    print(f'Invalid suit! Please choose from: {", ".join(suits)}')
                
                player.removeCard(c)
                deck_pile.append(c)
                print(f'THE CARD ON TOP IS {deck_pile[-1]}')
                print(f'Player 1 you now have: ')
                player.getCard()
                
            elif c.getFace() == deck_pile[-1].getFace() or c.getSuit() == deck_pile[-1].getSuit():
                player.removeCard(c)
                deck_pile.append(c)
                print(f'THE CARD ON TOP IS {deck_pile[-1]}')
                print(f'Player 1 you now have: ')
                player.getCard()
                chosen_suit_p1 = None  # Clear any previous suit choice
                
            else:
                print('WRONG CARD! You lost your turn, sorry :))))')
        
        # Check if player 1 won
        if not player.hasCard():
            break
        
        # ==================== PLAYER 2's TURN ====================
        print('\n' + '='*50)
        print('Player 2 will NOW PLAY')
        print('='*50)
        
        # Check if previous card was an 8 played by player 1
        if chosen_suit_p1 is not None and deck_pile[-1].getFace() == '8':
            print(f'The previous player chose suit: {chosen_suit_p1}')
            print(f'You must play a card with suit {chosen_suit_p1} or an 8')
            card_num = input("Enter the index of the card you want: ")
            
            # Validate input
            if not is_integer(card_num):
                print('INVALID INPUT! You lost your turn.')
                chosen_suit_p1 = None  # Reset after use
                continue
            
            c = player2.getSpecificCard(card_num)
            
            if not player2.trueCard(c):
                print('WRONG INDEX! You lost your turn.')
                chosen_suit_p1 = None
                continue
            
            # Check if card is valid (either an 8 or matches the chosen suit)
            if c.getFace() == '8':
                # Get valid suit choice
                while True:
                    chosen_suit_p2 = input('What suit do you choose? ').lower()
                    if chosen_suit_p2 in suits:
                        break
                    print(f'Invalid suit! Please choose from: {", ".join(suits)}')
                
                player2.removeCard(c)
                deck_pile.append(c)
                print(f'THE CARD ON TOP IS {deck_pile[-1]}')
                print(f'Player 2 you now have: ')
                player2.getCard()
                chosen_suit_p1 = None  # Reset after use
                
            elif c.getSuit().lower() == chosen_suit_p1.lower():
                player2.removeCard(c)
                deck_pile.append(c)
                print(f'THE CARD ON TOP IS {deck_pile[-1]}')
                print(f'Player 2 you now have: ')
                player2.getCard()
                chosen_suit_p1 = None  # Reset after use
                chosen_suit_p2 = None  # Clear P2's suit choice
                
            else:
                print('WRONG CARD! You lost your turn, sorry :))))')
                chosen_suit_p1 = None  # Reset after use
        
        else:
            # Normal turn - no 8 suit restriction
            chosen_suit_p1 = None  # Clear any previous 8 suit choice
            
            card_num = input("Enter the index of the card you want or write 'hit' if you want to draw cards: ")
            
            # If player wants to draw cards
            if card_num.lower() == 'hit':
                current = 0
                while current < 3:
                    ask = input("You can pick up to 3 cards! Write 'hit' to get a card and 'done' to stop: ")
                    if ask.lower() == 'hit':
                        current += 1
                        player2.addCard(warDeck.dealCard())
                        print(f'Now you have: ')
                        player2.getCard()
                    elif ask.lower() == 'done':
                        break
                    else:
                        print("WRONG INPUT - please write 'hit' or 'done'")
                
                # After drawing, player must play a card
                card_num = input("Enter the index of the card you want to play: ")
                
                if not is_integer(card_num):
                    print('INVALID INPUT! You lost your turn.')
                    continue
                
                c = player2.getSpecificCard(card_num)
                
            elif is_integer(card_num):
                c = player2.getSpecificCard(card_num)
                
            else:
                print('INVALID INPUT! You lost your turn.')
                continue
            
            # Validate the card exists
            if not player2.trueCard(c):
                print('WRONG INDEX! You lost your turn.')
                continue
            
            # Check if card is valid to play
            if c.getFace() == '8':
                # Get valid suit choice
                while True:
                    chosen_suit_p2 = input('What suit do you choose? ').lower()
                    if chosen_suit_p2 in suits:
                        break
                    print(f'Invalid suit! Please choose from: {", ".join(suits)}')
                
                player2.removeCard(c)
                deck_pile.append(c)
                print(f'THE CARD ON TOP IS {deck_pile[-1]}')
                print(f'Player 2 you now have: ')
                player2.getCard()
                
            elif c.getFace() == deck_pile[-1].getFace() or c.getSuit() == deck_pile[-1].getSuit():
                player2.removeCard(c)
                deck_pile.append(c)
                print(f'THE CARD ON TOP IS {deck_pile[-1]}')
                print(f'Player 2 you now have: ')
                player2.getCard()
                chosen_suit_p2 = None  # Clear any previous suit choice
                
            else:
                print('WRONG CARD! You lost your turn, sorry :))))')
        
        # Check if player 2 won
        if not player2.hasCard():
            break
    
    # CHECKING TO SEE WHO IS THE WINNER
    print('\n' + '='*50)
    if not player.hasCard():
        print('PLAYER 1 WINS!!!!')
    elif not player2.hasCard():
        print('PLAYER 2 WINS!!!!')
    print('='*50)


if __name__ == '__main__':
    playC()
