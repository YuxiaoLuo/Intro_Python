# this is program coin.py
# coin module
import random 

class Coin:
    
    def __init__(self):
        self.__sideup = 'Heads'
        
    # the toss method generates a random number 0 through 1
    # assigns to Heads or Tails
    
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
            
    # the get_sideup method return the value of 
    # data attribute __sideup
    
    def get_sideup(self):
        return self.__sideup
   