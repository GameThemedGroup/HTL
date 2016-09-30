package HTLProceduralAPI;

/**
 * @author Kunlakan (Jeen) Cherdchusilp
 * @author Tom Lai
 * 
 * ----------------------------------------------------------------------------
 * LAB 5 - Nested If: Moving Wizards
 * 
 * LEARNING OBJECTIVE:
 * 		Student will be able to demonstrate an understanding of nested if
 * 		statement
 * 
 * FUNCTIONS TO USE:
 * 		mouseClicked()
 * 
 * 		getClickedX()
 * 		getClickedY()
 * 
 * 		aWizardIsSelected()
 * 		tileHasWizard(int x, int y)
 * 		wizardIsSelected(int x, int y)
 * 		unselectWizard()
 * 		selectWizard(int x, int y)
 * 
 *	 	moveWizardTo(int x, int y)
 */

public class Lab5 extends HTLProceduralAPI
{	
	public void updateGame() {
		
		// Check if the mouse is clicked any where in the game scene
		if (mouseClicked()) {
			// Get the position of the mouse clicked
			int clickedX = getClickedX();
			int clickedY = getClickedY();

			// otherwise, if there's a Tower on the tile, toggle selection
			// of the tower
			if (tileHasWizard(clickedX, clickedY)) {

				if (wizardIsSelected(clickedX, clickedY)) {
					unselectWizard();
				} else {
					selectWizard(clickedX, clickedY);
				}
			}
			
			// if a Tower is selected, can it be moved to this Tile?
			else if (aWizardIsSelected()) {
				moveWizardTo(clickedX, clickedY);
			}
			
			// otherwise, place a Tower
			else {
				// either speedy or medic, pick one
				// drawMedicWizard(clickedColumn, clickedRow);
				drawSpeedyWizard(clickedX, clickedY);
				
			}

		}
		//makeWizardsFire();
		
		
	}
}
