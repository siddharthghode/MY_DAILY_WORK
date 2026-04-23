import java.util.Scanner;

public class ComputePI {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double summinus = 0.0;
        double sumplus = 1.0;   // FIX: include 1/1
        double total;

        System.out.println("Enter n:");
        int n = sc.nextInt();

        for (int i = 3; i <= n; i += 4) {
            summinus += 1.0 / i;
        }

        for (int i = 5; i <= n; i += 4) {
            sumplus += 1.0 / i;
        }

        total = 4 * (sumplus - summinus);

        System.out.println("The pi is: " + total);
    }
}