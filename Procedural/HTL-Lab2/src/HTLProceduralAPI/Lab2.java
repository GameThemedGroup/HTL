package HTLProceduralAPI;

/**
 * @author Kunlakan (Jeen) Cherdchusilp
 * @author Tom Lai
 * 
 * ----------------------------------------------------------------------------
 * LAB 2 - Method: Drawing Wizards with Parameters
 * 
 * LEARNING OBJECTIVE:
 * 		Student will be able to use a method/function that requires parameters
 * 
 * FUNCTIONS TO USE:
 * 		drawMedicWizard(int x, int y)
 * 		drawSpeedyWizard(int x, int y)
 * ----------------------------------------------------------------------------
 */
public class Lab2 extends HTLProceduralAPI
{
	public void buildGame()
	{
		drawMedicWizard(10, 9);  // x = 10, y = 9
		drawMedicWizard(10, 0);  // x = 10, y = 0
		
		drawSpeedyWizard(0, 5);  // x = 0,  y = 5
		drawSpeedyWizard(19, 5); // x = 19, y = 5
	}
	
}
