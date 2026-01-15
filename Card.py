'''
Created on Feb 8, 2022

@author: twendt
'''

class Card():
    """
    Represents a single playing card.

    A Card has:
    - face  (ex: "A", "2", "K")
    - suit  (ex: "Hearts", "Spades")
    - value (numeric value used for comparisons)
    - image (Tkinter image object used for drawing the card)
    """

    def __init__(self, face = None, suit = None, value = None, image = None):
        '''
        Constructor
        '''
        self.__suit = suit
        self.__face = face
        self.__value = value
        self.__image = image

    '''
    returns suit of card
    '''
    def getSuit(self):
        return self.__suit

    '''
    returns face of card
    '''
    def getFace(self):
        return self.__face

    """
    Returns the numeric value of the card.
    Used for comparisons between cards.
     """
    def getValue(self):
        return self.__value

    """
    Returns the image object associated with this card.
    (Used for drawing the card on a canvas.)
    """
    def getImage(self):
        return self.__image

    """
    Returns a readable string representation of the card.
    Example: "A of Hearts"
    """
    def __str__(self):
        return f"{self.__face} of {self.__suit}"

    """
    Draws the card image onto a Tkinter canvas.

    Parameters:
                cvs (Canvas): Tkinter Canvas to draw the card on
                left (int): x-position (left side)
                top (int): y-position (top side)
    """
    def draw(self, cvs, left, top):
        cvs.create_image(left, top, image = self.__image, anchor = "nw")
        
    
    '''
    Comparison methods.
    For the purposes of this course, we'll assume that all comparisons are done
    based on the face value of the cards.
    '''
    def __eq__(self, other):
        return self.getValue() == other.getValue()
    
    def __lt__(self, other):
        return self.getValue() < other.getValue()
    
    def __gt__(self, other):
        return self.getValue() > other.getValue()
    
    def __le__(self, other):
        return self < other or self == other
    
    def __ge__(self, other):
        return self > other or self == other
    
    def __ne__(self, other):
        return not (self == other)  