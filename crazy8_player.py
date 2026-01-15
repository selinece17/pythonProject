'''
Created on Mar 14, 2024
THIS PROGRAM HAS THE CLASS FOR THE CRAZY 8 PLAYER.

'''




class CPlayer(object):
    '''
    classdocs
    '''

    def __init__(self, name = "Gunes", parent = None, back = None):
        '''
        Constructor
        '''
        
        self.__name = name
        self.__cards = []
        self.__parent = parent
        self.__frame = None
        self.__canvas = None
        self.__back_of_card = back
        
        
    
            
    

    def addCard(self, card):
        '''
        Description: add the card f to the player's personal list
        Arguments: card: a single Card object
        Return: None
        '''
        self.__cards.append(card)
        
    def getCard(self):
        '''
        Description: prints out the cards the player has
        Arguments: card: nothing
        Return: the cards
        '''
        for i in range(len(self.__cards)):
            print(f"{self.__cards[i]}")

            
      
    
    
           

    def playCard(self):
        '''
        Description: Remove the first card in the list and return it.
                     If there are no cards, raise an exception
        Arguments:  None
        Return:     A card from the players hand.
        '''
        if self.hasCard():       
            myCard = self.__cards.pop(0)
            return myCard
        else:
            raise Exception("I don't have any cards, dummy.")
    
    def hasCard(self):
        '''
        Description: Returns True if the player has cards;
                     Returns False if the player has no cards.
        Arguments:  None
        Return:     boolean
        '''        
        if len(self.__cards) > 0:
            return True
        else:
            return False
        
    def cardsRemaining(self):
        '''
        Description: Returns the number of cards remaining in the player's hand
        Arguments:  None
        Return:     int - the number of cards in the player's hand
        '''          
        return len(self.__cards)
    
    
        
    def getSpecificCard(self,val):
        '''
        Description: gets the card the user wants 
        Arguments:  the index of the card that is in a list
        Return:     the specific card
        '''   
        
        for i in range(len(self.__cards)):
            if i==int(val):
                return self.__cards[i]
            
        return 'NOT FOUND'
        
    
    def trueCard(self,val): 
        '''
        Description: checks if the argument given is an actual card 
        Arguments:  a user input
        Return:     boolean
        ''' 
        try:
            val.getFace()  
            return True 
        
        except AttributeError:
            return False
             
        
     
     
    
    def finding(self,l):
        '''
        Description: finds the card the user gives as an argument
        Arguments:  a list that has the card name
        Return:    the specific card
        ''' 
        a=[]
        for i in range(len(self.__cards)):
            if self.__cards[i].getSuit().upper()==l[1].upper() and self.__cards[i].getFace()==l[0]:
                a.append(self.__cards[i])
        
        if len(a)==1:
            return a[0]
        else:
            return False
            
            
                
           
        
    def hasSpecificFace(self, val):
        '''
        Description: checks if the player has a specific face of a card
        Arguments:  face of a card
        Return:     boolean
        ''' 
        tot=0
        for i in range(len(self.__cards)):
            if self.__cards[i].getFace()==val:
                tot+=1
                
                
        if tot>0:
            return True 
    
       
    def hasSpecificSuit(self, val):
        '''
        Description: checks if the player has a specific suit of a card
        Arguments:  suit of a card
        Return:     boolean
        ''' 
        tot=0
        for i in range(len(self.__cards)):
            if self.__cards[i].getSuit().lower()==val.lower():
                tot+=1
                
                
        if tot>0:
            return True 
        
    def removeCard(self,s):
        '''
        Description: Remove the specific card the user gives as an argument.
                      If there are no cards, raise an exception
        Arguments:  a card
        Return:     remove the s card from the players hand.
        '''
        
        if self.hasCard():  
            a=[]
            
            for i in range(len(self.__cards)):
                if self.__cards[i].getSuit().upper()==s.getSuit().upper() and self.__cards[i].getFace()==s.getFace():
                    a.append(i)
                    
            
            if len(a)==1:
                self.__cards.pop(a[0])
            
            
            else:
                return 'Not found' 
        
            
                
        else:
            raise Exception("I don't have any cards, dummy.")
        
        
    

    
    def getName(self):
        '''
        Description: gets the name of the player
        Arguments:  None
        Return:     the player's name
        '''  
        return self.__name
    
    def setName(self, newName):
        '''
        Description: changes the name of the player with a new one
        Arguments:  None
        Return:     a new name for the player
        '''  
        if newName == "Ted Chan":
            print("Stop it.")
        else:
            self.__name = newName
            




if __name__ == "__main__":
    # Test our code to make sure it works.
    from Project1.DeckOfCards import DeckOfCards as DC
    from Project1.Card import Card
    
    status = "PASSED"
    K = 60
    
    print("Testing functionality of the CRAZY 8 Player class.")
############################
# Test default constructor #
############################
    message = "   Testing default constructor:"
    try:
        defaultWP = CPlayer()
        print(f"{message:<{K}} {'PASSED'}")
        
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during instantiation.")
        status = "FAILED"
        


#############################
# Test standard constructor #
#############################
    message = "   Testing standard constructor:"
    try:
        standardWP = CPlayer('Napoleon Guzelocak')
        if standardWP.getName() == 'Napoleon Guzelocak':
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Object instantiated, but name is wrong.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during instantiation.")
        print(f"      Exiting test.")
        status = "FAILED"
        exit()




#######################
# Test setName method #
#######################
    message = "   Testing 'setName' method:"
    try:
        standardWP.setName('Chris Tucker')
        if standardWP.getName() == 'Chris Tucker':
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but failed to set name.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED':>40s}")
        print(f"      Exception during setName method.")
        status = "FAILED"      

    
    

#####################################
# Test getCard method (empty hand) #
#####################################
    message = "   Testing 'getCard' method with empty hand:"
    try:
        if not standardWP.getCard():
            print(f"{message:<{K}} {'PASSED'}")
            
        else:        
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during getCard method.")
        status = "FAILED"
        
        
        

#####################################
# Test playCard method (empty hand) #
#####################################
    message = "   Testing 'playCard' method with empty hand:"
    try:
        standardWP.playCard()
        print(f"{message:<{K}} {'FAILED'}")
        status = "FAILED"   
    except:
        print(f"{message:<{K}} {'PASSED'}")


####################################
# Test hasCard method (empty hand) #
####################################
    message = "   Testing 'hasCard' method with empty hand:"
    try:
        if not standardWP.hasCard():
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during hasCard method.")
        status = "FAILED"    
        
        

###########################################
# Test cardsRemaining method (empty hand) #
###########################################
    message = "   Testing 'cardsRemaining' method with empty hand:"
    try:
        if standardWP.cardsRemaining() == 0:
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during cardsRemaining method.")
        status = "FAILED"
        
        


       

    
#####################################
# Test getSpecificCard method (non empty hand) #
#####################################
    message = "   Testing 'getSpecificCard' method with one card:"
    myDeck = DC()
    standardWP.addCard(myDeck.dealCard())
    try:
        if standardWP.getSpecificCard(0):
            print(f"{message:<{K}} {'PASSED'}")
            
        else:        
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during getSpecificCard method.")
        status = "FAILED"   
        
        
#####################################
# Test getCard method (non empty hand) #
#####################################
    message = "   Testing 'getCard' method with non empty hand:"
    try:
        standardWP.getCard()
        print(f"{message:<{K}} {'PASSED'}")
            
       
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during getCard method.")
        status = "FAILED"
             

####################################
# Test hasCard method (non empty hand) #
####################################
    message = "   Testing 'hasCard' method with non empty hand:"
    try:
        if  standardWP.hasCard():
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during hasCard method.")
        status = "FAILED"
        

####################################
# Test cardsRemaining method (non empty hand) #
####################################
    message = "   Testing 'cardsRemaining' method with non empty hand:"
    try:
        if  standardWP.cardsRemaining()==1:
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during cardsRemaining method.")
        status = "FAILED"    
        


        
###########################################
# Test finding method (non empty hand) #
###########################################
    message = "   Testing 'finding' method with one card:"
    cC=['A', 'Clubs']
    try:
        if standardWP.finding(cC):
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during cardsRemaining method.")
        status = "FAILED"      
        
        


        
        
###########################################
# Test hasSpecificSuit method (non empty hand) #
###########################################
    message = "   Testing 'hasSpecificSuit' method with one card:"
    try:
        if standardWP.hasSpecificSuit('CLUBS'):
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during hasSpecificSuit method.")
        status = "FAILED"
        
        
        
###########################################
# Test hasSpecificFace method (non empty hand) #
###########################################
    message = "   Testing 'hasSpecificFace' method with one card:"
    try:
        if standardWP.hasSpecificFace('A'):
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during hasSpecificFace method.")
        status = "FAILED"
        
        


###########################################
# Test trueCard method (non empty hand) #
###########################################
    message = "   Testing 'trueCard' method with one card:"
    try:
        if standardWP.trueCard(standardWP.playCard()):
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during removeCard method.")
        status = "FAILED"
        
        

