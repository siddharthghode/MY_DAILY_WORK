import java.util.Scanner;

public class PrintNNtimes {
    static void print(int i, int n) {
        if (i > n) return;
        System.out.println(n);
        print(i + 1, n);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the number you want to print n times");
        int n = sc.nextInt();
        print(1, n);
    }
}
