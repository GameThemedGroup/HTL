package HTLProceduralAPI;

/**
 * @author Kunlakan (Jeen) Cherdchusilp
 * @author Tom Lai
 * 
 * ----------------------------------------------------------------------------
 * LAB 10 - Gameplay: Win Conditions
 * 
 * LEARNING OBJECTIVE:
 * 		Student will be able to demonstrate an understanding of all concepts
 * 		learned from the previous labs.
 * 
 * FUNCTIONS TO USE:
 *		drawToolbars()
 *
 * 		updateScore(float score)
 * 		getNumOfWalkersSaved()
 * 		getHealthSaved()
 * 		getScore()
 *		enterWin();
 */

public class Lab10 extends HTLProceduralAPI {
	
	public void buildGame() {
		// Draw user interface to show game infromation
		drawToolbars();
		
		for (int currentNum = 0; currentNum < 20; currentNum = currentNum + 1) {
			addPathLeftRight(currentNum, 5);
		}

		preparePathForWalkers(0, 5, 19, 5);
	}

	public void updateGame() {
		// in-game
		
		if (countdownFired()) {
			// addBasicWalker()
			addQuickWalker();
		}
		
		// Check if current score passes the win condition
		checkGameWon();
		
		if (mouseClicked()) {
			int clickedX = getClickedX();
			int clickedY = getClickedY();

			if (tileHasWizard(clickedX, clickedY)) {

				if (wizardIsSelected(clickedX, clickedY)) {
					unselectWizard();
				} else {
					selectWizard(clickedX, clickedY);
				}
			}
			
			else if (aWizardIsSelected()) {
				moveWizardTo(clickedX, clickedY);
			}
			
			else {
				// drawMedicWizard(clickedColumn, clickedRow);
				drawSpeedyWizard(clickedX, clickedY);
				
			}

		}


		for (int i = 0; i < numOfWizards(); i++) {
			if (wizardIsReady(i)) {
				for (int j = 0; j < numOfWalkers(); j++) {
					if (walkerIsInRange(i, j)) {
						if (wizardIsMedic(i)) {
							medicWizardCastSpellOnWalker(i, j);
						} else {
							speedyWizardCastSpellOnWalker(i, j);
						}
					}
				}
			}
		}

		// Update the current score
		updateScore(getNumOfWalkersSaved() * getHealthSaved());
	}
	
	// Check if current score passes the win condition
	public void checkGameWon() {
		if( getScore() >= 500 ){
			enterWin();
		}
	}
}
