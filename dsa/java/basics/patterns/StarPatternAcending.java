import java.util.Scanner;

public class StarPatternAcending {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter num:");
        int n = sc.nextInt();
        System.out.println();
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= i; j++) System.out.print("*");
            System.out.println();
        }
    }
}
