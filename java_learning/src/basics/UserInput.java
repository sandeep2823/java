package basics;

import java.util.Scanner;

public class UserInput {

	static Scanner input = new Scanner(System.in);
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.print("Enter A Value: ");
		
		if(input.hasNextInt()){
			int numberEntered = input.nextInt();
			System.out.println("You Entered " + numberEntered);

		}
		
		else {
			System.out.println("Enter An Integer Value Next Time.");
		}

	}

}
