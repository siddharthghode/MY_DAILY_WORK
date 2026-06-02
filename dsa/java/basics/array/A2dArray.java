import java.util.Scanner;

public class A2dArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Give size of 2D array:");
        int a = sc.nextInt(), b = sc.nextInt();
        int[][] c = new int[a][b];
        System.out.println("Enter elements for 2D array of " + a + "X" + b + ":");
        for (int i = 0; i < a; i++) for (int j = 0; j < b; j++) c[i][j] = sc.nextInt();
        System.out.println("Entered elements are:");
        for (int i = 0; i < a; i++) {
            for (int j = 0; j < b; j++) System.out.print(c[i][j] + " ");
            System.out.println();
        }
    }
}
