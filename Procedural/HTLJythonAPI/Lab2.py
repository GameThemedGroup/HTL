'''
@author: Taran Christensen
'''
from HTLAPISupport import *

@build_Game
def buildGame(Game):
    Game.drawMedicWizard(10,9)  # x = 10, y = 9
    Game.drawMedicWizard(10,0)  # x = 10, y = 0
    Game.drawSpeedyWizard(0,5)  # x = 0,  y = 5
    Game.drawSpeedyWizard(19,5) # x = 19, y = 5

startProgram()