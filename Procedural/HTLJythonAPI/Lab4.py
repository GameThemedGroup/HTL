'''
@author: Taran Christensen
'''
from HTLAPISupport import *

#Declare variables for the start position of the "player wizard" 
x = 0;
y = 0;
    
@build_Game
def buildGame(Game):
    # Player wizard start position
    Game.drawSpeedyWizard(0,0);
    
    # Build the maze board!
    Game.drawMedicWizard(1,1);
    Game.drawMedicWizard(2, 1);
    Game.drawMedicWizard(3, 1);
    Game.drawMedicWizard(4, 1);
    Game.drawMedicWizard(5, 1);
    Game.drawMedicWizard(6, 1);
    Game.drawMedicWizard(7, 1);
    Game.drawMedicWizard(8, 1);
    Game.drawMedicWizard(18, 1);
    Game.drawMedicWizard(19, 1);
    Game.drawMedicWizard(20, 1);
    
    Game.drawMedicWizard(1, 2);
    Game.drawMedicWizard(2, 2);
    Game.drawMedicWizard(3, 2);
    Game.drawMedicWizard(4, 2);
    Game.drawMedicWizard(5, 2);
    Game.drawMedicWizard(6, 2);
    Game.drawMedicWizard(7, 2);
    Game.drawMedicWizard(8, 2);
    Game.drawMedicWizard(10, 2);
    Game.drawMedicWizard(11, 2);
    Game.drawMedicWizard(12, 2);
    Game.drawMedicWizard(13, 2);
    Game.drawMedicWizard(14, 2);
    Game.drawMedicWizard(15, 2);
    Game.drawMedicWizard(16, 2);

    
    Game.drawMedicWizard(5, 3);
    Game.drawMedicWizard(8, 3);
    Game.drawMedicWizard(10, 3);
    Game.drawMedicWizard(11, 3);
    Game.drawMedicWizard(12, 3);
    Game.drawMedicWizard(13, 3);
    Game.drawMedicWizard(14, 3);
    Game.drawMedicWizard(15, 3);
    Game.drawMedicWizard(16, 3);
    Game.drawMedicWizard(18, 3);
    Game.drawMedicWizard(19, 3);
    Game.drawMedicWizard(20, 3);

    Game.drawMedicWizard(0, 4);
    Game.drawMedicWizard(2, 4);
    Game.drawMedicWizard(3, 4);
    Game.drawMedicWizard(5, 4);
    Game.drawMedicWizard(6, 4);
    Game.drawMedicWizard(8, 4);
    Game.drawMedicWizard(10, 4);
    Game.drawMedicWizard(11, 4);
    Game.drawMedicWizard(12, 4);
    Game.drawMedicWizard(13, 4);
    Game.drawMedicWizard(14, 4);
    Game.drawMedicWizard(15, 4);
    Game.drawMedicWizard(16, 4);
    Game.drawMedicWizard(18, 4);
    Game.drawMedicWizard(19, 4);
    Game.drawMedicWizard(20, 4);
    
    Game.drawMedicWizard(0, 5);
    Game.drawMedicWizard(2, 5);
    Game.drawMedicWizard(3, 5);
    Game.drawMedicWizard(5, 5);
    Game.drawMedicWizard(6, 5);
    Game.drawMedicWizard(8, 5);
    Game.drawMedicWizard(16, 5);
    Game.drawMedicWizard(18, 5);
    Game.drawMedicWizard(19, 5);
    Game.drawMedicWizard(20, 5);
    
    Game.drawMedicWizard(0, 6);
    Game.drawMedicWizard(5, 6);
    Game.drawMedicWizard(6, 6);
    Game.drawMedicWizard(8, 6);
    Game.drawMedicWizard(9, 6);
    Game.drawMedicWizard(10, 6);
    Game.drawMedicWizard(11, 6);
    Game.drawMedicWizard(12, 6);
    Game.drawMedicWizard(13, 6);
    Game.drawMedicWizard(14, 6);
    Game.drawMedicWizard(16, 6);
    Game.drawMedicWizard(18, 6);
    Game.drawMedicWizard(19, 6);
    Game.drawMedicWizard(20, 6);
    
    Game.drawMedicWizard(0, 7);
    Game.drawMedicWizard(1, 7);
    Game.drawMedicWizard(2, 7);
    Game.drawMedicWizard(3, 7);
    Game.drawMedicWizard(5, 7);
    Game.drawMedicWizard(6, 7);
    Game.drawMedicWizard(8, 7);
    Game.drawMedicWizard(9, 7);
    Game.drawMedicWizard(10, 7);
    Game.drawMedicWizard(11, 7);
    Game.drawMedicWizard(12, 7);
    Game.drawMedicWizard(13, 7);
    Game.drawMedicWizard(14, 7);
    Game.drawMedicWizard(16, 7);
    Game.drawMedicWizard(18, 7);
    Game.drawMedicWizard(19, 7);
    Game.drawMedicWizard(20, 7);
   
    Game.drawMedicWizard(0, 8);
    Game.drawMedicWizard(1, 8);
    Game.drawMedicWizard(2, 8);
    Game.drawMedicWizard(3, 8);
    Game.drawMedicWizard(16, 8);
    Game.drawMedicWizard(18, 8);
    Game.drawMedicWizard(19, 8);
    Game.drawMedicWizard(20, 8);
    
    Game.drawMedicWizard(0, 9);
    Game.drawMedicWizard(1, 9);
    Game.drawMedicWizard(2, 9);
    Game.drawMedicWizard(3, 9);
    Game.drawMedicWizard(5, 9);
    Game.drawMedicWizard(6, 9);
    Game.drawMedicWizard(7, 9);
    Game.drawMedicWizard(8, 9);
    Game.drawMedicWizard(9, 9);
    Game.drawMedicWizard(10, 9);
    Game.drawMedicWizard(11, 9);
    Game.drawMedicWizard(12, 9);
    Game.drawMedicWizard(13, 9);
    Game.drawMedicWizard(14, 9);
    Game.drawMedicWizard(15, 9);
    Game.drawMedicWizard(16, 9);
    
@update_Game
def updateGame(Game):
    # To *change* the global x and y variables, you need
    #  to tell the method that these two variables are
    #  in fact global. Otherwise it will attempt to make
    #  local versions of them. Because Python.
    global x
    global y
    
    if Game.keyboardIsPressingRight():
        x = x + 1;
        Game.drawSpeedyWizard(x, y);
    elif Game.keyboardIsPressingLeft():
        x = x - 1;
        Game.drawSpeedyWizard(x, y);
    elif Game.keyboardIsPressingUp():
        y = y + 1;
        Game.drawSpeedyWizard(x, y);
    elif Game.keyboardIsPressingDown(): 
        y = y - 1;
        Game.drawSpeedyWizard(x, y);

startProgram()