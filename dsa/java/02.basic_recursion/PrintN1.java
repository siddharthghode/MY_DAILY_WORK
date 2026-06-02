import java.util.Scanner;

public class PrintN1 {
    static void print(int i, int n) {
        if (i > n) return;
        System.out.println(n);
        print(i, n - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the number from which you want to print numbers reverse");
        int n = sc.nextInt();
        print(1, n);
    }
}
