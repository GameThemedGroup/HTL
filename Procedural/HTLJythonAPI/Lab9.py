'''
@author: Taran Christensen
'''
from HTLAPISupport import *

@build_Game
def buildGame(Game):
    for currentNum in range(0, 20):
        Game.addPathLeftRight(currentNum, 5);
        
    Game.preparePathForWalkers(0,5,19,5);
    Game.setCountdownFrom(3);

@update_Game
def updateGame(Game):
    if Game.countdownFired():
        Game.addQuickWalker();
    

    # in-game
    if Game.mouseClicked():
        clickedRow = Game.getClickedRow()
        clickedColumn = Game.getClickedColumn()
        
        # if a Tower is selected, can it be moved to this Tile?
        if Game.aWizardIsSelected():
            Game.moveWizardTo(clickedColumn, clickedRow)
        
        # otherwise, if there's a Tower on the tile, toggle selection
        #  of the tower
        elif Game.tileHasWizard(clickedColumn, clickedRow):
            
            if Game.wizardIsSelected(clickedColumn, clickedRow):
                Game.unselectWizard()
            else: 
                Game.selectWizard(clickedColumn, clickedRow)
                
        # otherwise, place a Tower
        else:
            # either speedy or medic, pick one
            # drawMedicWizard(clickedColumn, clickedRow);
            Game.drawSpeedyWizard(clickedColumn, clickedRow);
    
    # heal walkers or make walkers faster
    for i in range(0, Game.numOfWizards()):
        for j in range(0, Game.numOfWalkers()):
            if Game.walkerIsInRange(i, j):
                # either speedy or medic, pick one
                # medicWizardCastSpellOnWalker(i, j);
                Game.speedyWizardCastSpellOnWalker(i, j);

startProgram()