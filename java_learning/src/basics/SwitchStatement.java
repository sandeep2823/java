package basics;

public class SwitchStatement {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		char grade = 'a';
		switch (grade) {
		case 'A':
		case 'a':
			System.out.println("good job");
			break;
		case 'B':
		case 'b':
			System.out.println("fair job");
			break;
		case 'C':
		case 'c':
			System.out.println("you can do better");
			break;
		default:
			System.out.println("not a great job");
			break;
		}

	}

}
