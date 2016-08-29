package HTLProceduralAPI;

/**
 * @author Kunlakan (Jeen) Cherdchusilp
 * @author Tom Lai
 * 
 * ----------------------------------------------------------------------------
 * LAB 8 - While Loop: What Is While Loop?
 * 
 * LEARNING OBJECTIVE:
 * 		Student will be able to demonstrate an understanding of the concept by
 * 		drawing completed custom paths by using while loops, and the different
 * 		and the similarity between for loop and while loop
 */

public class Lab8 extends HTLProceduralAPI
{	
	public void buildGame()
	{
		// 1. Make paths
		/*      9| 
		 *      8| 
		 *      7| 
		 *      6|               
		 *   y  5| X X X X X X X X X X X
		 *      4|                    
		 *      3|                
		 *      2|                
		 *      1|                
		 *      0|______________________
		 *         0 1 2 3 4 5 6 7 8 9 ...
		 *            		x
		 */
		
		int currentNum = 0;
		while (currentNum < 20) {
			addPathLeftRight(currentNum, 5);
			currentNum = currentNum + 1;
		}

	}
	
	public void updateGame() {

		if (countdownFired()) {
			addBasicWalker();
			//addQuickWalker();
		}
	}
}
