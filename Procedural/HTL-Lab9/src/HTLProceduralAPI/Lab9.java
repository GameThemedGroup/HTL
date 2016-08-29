package HTLProceduralAPI;

/**
 * @author Kunlakan (Jeen) Cherdchusilp
 * @author Tom Lai
 * 
 * ----------------------------------------------------------------------------
 * Lab 9 - Nested For Loop: Make Wizards Casting Spells
 * 
 * LEARNING OBJECTIVE:
 * 		Student will be able to demonstrate an understanding of the concept of
 * 		by using nested for loop to make wizards casting spells on walkers if
 * 		there are nearby
 * 
 * FUNCTIONS TO USE:
 * 		numOfWizards()
 * 		numOfWalkers()
 * 
 * 		walkerIsInRange(int towerID, int walkerID)
 * 
 * 		medicWizardCastSpellOnWalker(int towerID, int walkerID)
 * 		speedyWizardCastSpellOnWalker(int towerID, int walkerID)
 */

public class Lab9 extends HTLProceduralAPI
{	
	public void buildGame()
	{			
		for (int currentNum = 0; currentNum < 20; currentNum = currentNum + 1) {
			addPathLeftRight(currentNum, 5);
		}
		
		preparePathForWalkers(0,5,19,5);
	}
	
	
	public void updateGame() {
		
		if (countdownFired()) {
			// addBasicWalker()
			addQuickWalker();
		}

		
		// in-game
		if (mouseClicked()) {
			int clickedX = getClickedX();
			int clickedY = getClickedY();
			
			// if a Tower is selected, can it be moved to this Tile?
			if (aWizardIsSelected()) {
				moveWizardTo(clickedX, clickedY);
			}
			// otherwise, if there's a Tower on the tile, toggle selection
			// of the tower
			else if (tileHasWizard(clickedX, clickedY)) {

				if (wizardIsSelected(clickedX, clickedY)) {
					unselectWizard();
				} else {
					selectWizard(clickedX, clickedY);
				}
			}
			// otherwise, place a Tower
			else {
				// either speedy or medic, pick one
				// drawMedicWizard(clickedColumn, clickedRow);
				drawSpeedyWizard(clickedX, clickedY);
				
			}

		}
		
		
		// heal walkers or make walkers faster
		for (int i = 0; i < numOfWizards(); i++) {
			for (int j = 0; j < numOfWalkers(); j++) {
				if (walkerIsInRange(i, j)) {
					// either speedy or medic, pick one
					// medicWizardCastSpellOnWalker(i, j);
					speedyWizardCastSpellOnWalker(i, j);
				}
			}
		}

		
	}
}
