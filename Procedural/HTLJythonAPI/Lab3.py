'''
@author: Taran Christensen
'''
from HTLAPISupport import *

@update_Game
def updateGame(Game):
    if Game.keyboardIsPressingRight():
        Game.drawSpeedyWizard(19, 5)    # x = 19, y = 5
    elif Game.keyboardIsPressingLeft():
        Game.drawSpeedyWizard(0, 5);    # x = 0, y = 5
    elif Game.keyboardIsPressingUp():
        Game.drawMedicWizard(10, 9);    # x = 10, y = 9
    elif Game.keyboardIsPressingDown(): 
        Game.drawMedicWizard(10, 0);    # x = 10, y = 0

startProgram()