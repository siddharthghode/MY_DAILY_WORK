import java.util.Scanner;

public class CheckDivisibleByK {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = {12, 15, 18, 20, 25, 30, 33, 35, 40, 45};
        System.out.print("enter the number you want to check and the divisor K: ");
        int K = sc.nextInt();
        int count = 0;
        for (int x : arr) if (x % K == 0) count++;
        System.out.println(count);
    }
}
