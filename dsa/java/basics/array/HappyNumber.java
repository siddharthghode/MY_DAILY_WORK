import java.util.HashSet;
import java.util.Scanner;

public class HappyNumber {
    static boolean isHappy(int n) {
        HashSet<Integer> seen = new HashSet<>();
        while (true) {
            int sum = 0;
            while (n > 0) { int d = n % 10; sum += d * d; n /= 10; }
            if (sum == 1) return true;
            if (!seen.add(sum)) return false;
            n = sum;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        System.out.println(num + (isHappy(num) ? " is a Happy Number" : " is NOT a Happy Number"));
    }
}
