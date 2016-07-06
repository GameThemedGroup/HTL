'''
@author: Taran Christensen
'''
from HTLAPISupport import *

@update_Game
def updateGame(Game):
    # in-game
    if Game.mouseClicked():
        clickedRow = Game.getClickedRow();
        clickedColumn = Game.getClickedColumn();
        
        # if a Tower is selected, can it be moved to this Tile?
        if Game.aWizardIsSelected():
            Game.moveWizardTo(clickedColumn, clickedRow);
        
        # otherwise, if there's a Tower on the tile, toggle selection
        #  of the tower
        elif Game.tileHasWizard(clickedColumn, clickedRow):

            if Game.wizardIsSelected(clickedColumn, clickedRow):
                Game.unselectWizard();
            else:
                Game.selectWizard(clickedColumn, clickedRow);
            
        # otherwise, place a Tower
        else:
            # either speedy or medic, pick one
            # drawMedicWizard(clickedColumn, clickedRow);
            Game.drawSpeedyWizard(clickedColumn, clickedRow);
         

    
    Game.makeWizardsFire();

startProgram()