'''
@author: Taran Christensen
'''
from HTLAPISupport import *

@build_Game
def buildGame(Game):
    """
    1. Make paths
          9| 
          8| 
          7| 
          6|               
     rows 5| X X X X X X X X X X X
          4|                    
          3|                
          2|                
          1|                
          0|______________________
             0 1 2 3 4 5 6 7 8 9 ...
                columns
    """
    
    currentNum = 0
    
    while currentNum < 20:
        Game.addPathLeftRight(currentNum, 5);
        currentNum = currentNum + 1;
    
    Game.preparePathForWalkers(0,5,19,5);

@update_Game
def updateGame(Game):
    if Game.countdownFired():
        Game.addBasicWalker();

startProgram()