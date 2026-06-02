import java.util.Scanner;

public class FactorialFuction {
    static int factorial(int n) {
        int fact = 1;
        for (int i = 1; i <= n; i++) fact *= i;
        return fact;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number for factorial");
        int n = sc.nextInt();
        System.out.println(factorial(n));
    }
}
