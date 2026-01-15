'''
Created on Feb 8, 2022

@author: twendt
'''

from PIL import Image, ImageTk
from Project1.Card import Card
import random

class DeckOfCards(object):
    """
    Represents a standard 52-card deck.

    This class can optionally load card images from a sprite sheet and attach
    an image to each Card object.

    Class Variables:
           size (int): Total number of cards in the deck (52).
           suits (list): List of card suit names.
           faces (list): List of card face names.
           cardImages (PIL.Image): The full sprite sheet image containing all cards.
           width (int): Width of each individual card image in the sprite sheet.
           height (int): Height of each individual card image in the sprite sheet.
    """

    size = 52
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cardImages = None
    width = 0
    height = 0


    @classmethod
    def loadCardImages(cls, filename):
        """
        Loads the deck image sprite sheet from the ../img directory.

        The sprite sheet is expected to contain all cards arranged in:
         - 13 columns (A through K)
         - 5 rows (Clubs, Diamonds, Hearts, Spades, plus the back row)

          This method calculates each individual card's width and height.

          Parameters:
                    filename (str): Name of the image file inside ../img/
          """
        try:
            DeckOfCards.cardImages = Image.open(f"../img/{filename}")
            DeckOfCards.width, DeckOfCards.height = DeckOfCards.cardImages.size
            DeckOfCards.width //= 13
            DeckOfCards.height //= 5
            
        except FileNotFoundError:
            print(f"File '{filename}' cannot be found in the directory '../img'.")
        except:
            print("An error occurred loading your image")
            
    @classmethod
    def __loadImage(self, row, col):
        '''
        preconditions: 
          * The class 'cardImages' file has been opened.
          * The image for the deck has the cards arranged in 13 rows and 4 columns.
          * The columns are ordered A-2-3-4-...-J-Q-K
          * The rows are ordered Clubs-Diamonds-Hearts-Spades
          * The 'back' image for the cards is in the fifth row in the third column (i.e row = 4, col = 2)
        postconditions:
          * The 'cropped' image for this card is returned.
        '''
        assert DeckOfCards.cardImages is not None
        assert DeckOfCards.width > 0
        assert DeckOfCards.height > 0

        img = DeckOfCards.cardImages.crop((col*DeckOfCards.width, 
                                           row*DeckOfCards.height,
                                           (col + 1)*DeckOfCards.width,
                                            (row + 1)*DeckOfCards.height))
        t = ImageTk.PhotoImage(img)
        return t    
            
    def __init__(self, deckImages = None):
        """
        Constructor for DeckOfCards.

        If an image sprite sheet name is provided, this deck loads images
        and stores a Card object for the "back of card" image.

        Parameters:
            deckImages (str or None):
                - If a filename is provided, load images from ../img/filename.
                - If None, cards will be created without images.
        """
        if deckImages is not None:
            DeckOfCards.loadCardImages(deckImages)
            self.backOfCard = Card(None, None, 0, DeckOfCards.__loadImage(4, 2))
        else:
            self.backOfCard = None
            
        # Create a deck
        self.__cards = []
        self.currentCard = 0
        for i in range(len(DeckOfCards.faces)):
            for j in range(len(DeckOfCards.suits)):
                face = DeckOfCards.faces[i]
                suit = DeckOfCards.suits[j]
                value = i
                if deckImages is not None:
                    img = DeckOfCards.__loadImage(j, i)
                else:
                    img = None
                self.__cards.append(Card(face, suit, value, img))


    def shuffle(self):
        """
        Shuffles the deck randomly.
        """
        random.shuffle(self.__cards)
        
    def dealCard(self):
        """
        Deals (returns) the next card from the deck.

        If the deck is empty, returns None.

        Returns:
           Card or None: The next card in the deck, or None if no cards remain
        """
        if not self.isEmpty():
            c = self.__cards[self.currentCard]
            self.currentCard += 1
        else:
            c = None
        return c
        
    def cardsRemaining(self):
        """
        Returns how many cards remain undealt in the deck.

        Returns:
            int: number of remaining cards
        """
        return len(self.__cards) - self.currentCard
    
    def isEmpty(self):
        """
        Returns True if no cards remain to be dealt.

        Returns:
            bool: True if the deck is empty, False otherwise
        """
        return self.cardsRemaining() == 0
    
    def hasNext(self):
        """
        Returns True if the deck still has a next card to deal.

        Returns:
            bool: True if there are cards remaining, False otherwise
        """
        return not self.isEmpty() 
    
    
    
    def reset(self):
        """
        Resets the deck back to the top (so dealing starts from the beginning again).
        Does NOT reshuffle the deck.
        """
        self.currentCard = 0
        
        