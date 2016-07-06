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
    
    
    PRE-BUILT PATH USED FOR DEMONSTRATION
    Game.addPathLeftRight(0, 5);
    Game.addPathLeftRight(1, 5);
    Game.addPathLeftRight(2, 5);
    Game.addPathLeftRight(3, 5);
    Game.addPathLeftRight(4, 5);
    Game.addPathLeftRight(5, 5);
    Game.addPathLeftRight(6, 5);
    Game.addPathLeftRight(7, 5);
    Game.addPathLeftRight(8, 5);
    Game.addPathLeftRight(9, 5);
    Game.addPathLeftRight(10, 5);
    Game.addPathLeftRight(11, 5);
    Game.addPathLeftRight(12, 5);
    Game.addPathLeftRight(13, 5);
    Game.addPathLeftRight(14, 5);
    Game.addPathLeftRight(15, 5);
    Game.addPathLeftRight(16, 5);
    Game.addPathLeftRight(17, 5);
    Game.addPathLeftRight(18, 5);
    Game.addPathLeftRight(19, 5);
    """
    
    for currentNum in range(0, 20):
        Game.addPathLeftRight(currentNum, 5);
        
    Game.preparePathForWalkers(0,5,19,5);

@update_Game
def updateGame(Game):
    if Game.countdownFired():
        Game.addBasicWalker();

startProgram()