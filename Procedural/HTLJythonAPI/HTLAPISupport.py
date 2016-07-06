'''

@author: Taran Christensen
'''

# We use an underscore to hide the "GameWindow" when this module is imported.
from Engine import GameWindow as _GameWindow
from HTL_API import *
from HTLProceduralAPI import HTLProceduralAPI

class CustomHTLMaker(HTLProceduralAPI):
    
    """Variables used to store references to the overwrite-able methods"""
    doBuildGame = None
    doUpdateGame = None
    
    """The methods below determine whether or not the given methods are being overwritten by the student. 
    If the methods are being overwritten, the method itself is stored in a variable. If it is not, the
    superclass's method is stored instead. """
    def buildGame(self):
        if CustomHTLMaker.doBuildGame is not None:
            CustomHTLMaker.doBuildGame(self)
        else:
            super(CustomHTLMaker, self).buildGame() 
            
    def updateGame(self):
        if CustomHTLMaker.doUpdateGame is not None:
            CustomHTLMaker.doUpdateGame(self)
        else:
            super(CustomHTLMaker, self).updateGame() 
    
"""These methods form annotations to be used by the student, as detailed below."""       
# This function will later be used as an annotation. It sets the function to be called
# in order to build the game.
#
# Example usage:
#
# | @build_Game
# | def my_init(CustomHTLMaker):
# |     <do something here>
#
# Python will translate this to:
#
# | def my_init(CustomHTLMaker):
# |     <do something here>
# | my_init = build_Game(my_init)

def build_Game(f):
    CustomHTLMaker.doBuildGame = f
    return f;

def update_Game(f):
    CustomHTLMaker.doUpdateGame = f
    return f;

class _Main(_GameWindow):

    """Python constructor"""
    def __init__(self):
        super(_GameWindow, self).__init__()
        self.gameMaker = CustomHTLMaker()
        self.setRunner(self.gameMaker)

def startProgram(showFlashScreen = False):
    """Start the program."""
    m = _Main()
    m.startProgram()
