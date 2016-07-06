'''
@author: Taran Christensen
'''
from HTLAPISupport import *

defaultWizardType = "medic";
defaultWalkerType = "basic";

@build_Game
def buildGame(Game):
    Game.drawToolbars();
    for currentNum in range(0, 20): 
        Game.addPathLeftRight(currentNum, 5)

    Game.preparePathForWalkers(0, 5, 19, 5)
    Game.setWalkerDamagePerSecond(5)
    Game.setCountdownFrom(3.5)
    Game.setScoreToWin(5000)

@update_Game
def updateGame(Game):
    # Inform Python that you're going to change these global variables
    #  in this method, so that it doesn't make local ones instead
    global defaultWizardType
    global defaultWalkerType
    
    if Game.countdownFired():
        Game.addWalker(defaultWalkerType)
    
    # in-game
    if Game.userWon():
        Game.enterWin();

    if Game.mouseClicked(): 
        clickedRow = Game.getClickedRow();
        clickedColumn = Game.getClickedColumn();
        if Game.userWon(): # if user won, check for button clicks
            if Game.winRestartButtonSelected(): # did user click on the restart button?
                Game.enterGameplay();
            elif Game.winQuitButtonSelected():  # or did user click on the quit button?
                Game.exitGame();
        else:
            # if a Tower is selected, can it be moved to this Tile?
            if Game.aWizardIsSelected():
                Game.moveWizardTo(clickedColumn, clickedRow)
            # otherwise, if there's a Tower on the tile, toggle selection
            # of the tower
            elif Game.tileHasWizard(clickedColumn, clickedRow):
                if Game.wizardIsSelected(clickedColumn, clickedRow):
                    Game.unselectWizard()
                else:
                    Game.selectWizard(clickedColumn, clickedRow)
            # otherwise, place a Tower
            else:
                # either speedy or medic
                Game.drawWizard(clickedColumn, clickedRow, defaultWizardType)

    if Game.keyboardIsPressingLeft():
        defaultWizardType = "medic"
    elif Game.keyboardIsPressingRight():   
        defaultWizardType = "speedy"
    elif Game.keyboardIsPressingUp():
        defaultWalkerType = "quick"
    elif Game.keyboardIsPressingUp():
        defaultWalkerType = "basic"

    # heal walkers or make walkers faster
    for i in range(0, Game.numOfWizards()):
        if Game.wizardIsReady(i):
            for j in range(0, Game.numOfWalkers()):
                if Game.walkerIsInRange(i, j):
                    if Game.wizardIsMedic(i):
                        Game.medicWizardCastSpellOnWalker(i, j);
                    else:
                        Game.speedyWizardCastSpellOnWalker(i, j);

    Game.setScore(Game.getNumOfWalkersSaved() * Game.getHealthSaved());

startProgram()