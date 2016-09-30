package HTLProceduralAPI;

/**
 * @author Kunlakan (Jeen) Cherdchusilp
 * @author Tom Lai
 * 
 * ----------------------------------------------------------------------------
 * LAB 11 - Gameplay: Cleanup The Game!
 * 
 * LEARNING OBJECTIVE:
 * 		Student will be able to demonstrate an understanding of all concepts
 * 		learned from the previous labs.
 * 
 * FUNCTIONS TO USE:
 * 		addWalker(String type)
 *		drawWizard(int x, int y, String type)
 *
 * 		setWalkerDamagePerSecond(int damage)
 * 		setCountdown(double seconds)
 * 		setScoreToWin(float scoreToWin)
 * 		setSpeedyTimeBetweenSpellcasts(double duration)
 * 		setMedicTimeBetweenSpellcasts(double duration)
 * 		setMedicWizardHealthAdjust(double health)
 * 		setSpeedyWizardSpeedBoostDuration(double duration)
 *		setSpeedyWizardSpeedBoostMultipler(double multiplier)
 */

public class Lab11 extends HTLProceduralAPI {
	String defaultWizardType = "medic";
	String defaultWalkerType = "basic";

	public void buildGame() {
		drawToolbars();
		
		for (int currentNum = 0; currentNum < 20; currentNum = currentNum + 1) {
			addPathLeftRight(currentNum, 5);
		}

		preparePathForWalkers(0, 5, 19, 5);

		// Settings
		setWalkerDamagePerSecond(5);
		setCountdown(3);
		setScoreToWin(1);
		setSpeedyTimeBetweenSpellcasts(1.0);
		setMedicTimeBetweenSpellcasts(3.0);
		//setMedicWizardHealthAdjust(10.0);
		setMedicWizardHealthAdjust(-10.0);
		setSpeedyWizardSpeedBoostDuration(1.0);
		// setSpeedyWizardSpeedBoostMultipler(3.0);
		setSpeedyWizardSpeedBoostMultipler(-3.0); // if negative, walker goes
													// backwards
	}

	public void updateGame() {

		if (keyboardIsPressingLeft()) {
			defaultWizardType = "medic";
		}
		else if (keyboardIsPressingRight()) {
			defaultWizardType = "speedy";
		}
		else if (keyboardIsPressingUp()) {
			defaultWalkerType = "quick";
		}
		else if (keyboardIsPressingUp()) {
			defaultWalkerType = "basic";
		}
		
		if (countdownFired()) {
			addWalker(defaultWalkerType);
		}

		// in-game
		checkGameWon();

		if (mouseClicked()) {
			int clickedX = getClickedX();
			int clickedY = getClickedY();
			
			
			if (tileHasWizard(clickedX, clickedY)) {
				if (wizardIsSelected(clickedX, clickedY)) {
					unselectWizard();
				}
				else {
					selectWizard(clickedX, clickedY);
				}
			}
			else if (aWizardIsSelected()) {
				moveWizardTo(clickedX, clickedY);
			}
			else {
				// either speedy or medic
				drawWizard(clickedX, clickedY, defaultWizardType);
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
		updateScore(getNumOfWalkersSaved() * getHealthSaved());
	}
	
	public void checkGameWon() {
		if( getScore() >= 500 ){
			enterWin();
		}
	}
}
