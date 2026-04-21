import java.util.InputMismatchException;
import java.util.Scanner;

public class Exception_handling_01 {
    public static void main(String[] args) {

        System.out.println("Enter the inputs");
        Scanner sc = new Scanner(System.in);

        try {
            int x = sc.nextInt();
            int y = sc.nextInt();

            int result = x / y;  // use int to trigger exception
            System.out.println("Result: " + result);
        }
        catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero");
        }
        catch (InputMismatchException e) {
            System.out.println("Input Mismatch Error");
        }
        catch (Exception e) {
            System.out.println("General Error");
        }
    }
}