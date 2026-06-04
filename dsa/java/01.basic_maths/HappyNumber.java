import java.util.*;

public class HappyNumber {
    static boolean isHappy(int num) {
        HashSet<Integer> seen = new HashSet<>();
        while (true) {
            int sum = 0;
            while (num > 0) { int d = num % 10; sum += d * d; num /= 10; }
            if (sum == 1) return true;
            if (!seen.add(sum)) return false;
            num = sum;
        }
    }

    public static void main(String[] args) {
        System.out.println(isHappy(19));
    }
}
