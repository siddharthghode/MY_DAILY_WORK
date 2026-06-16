import java.util.*;

public class A06_count_maximum_one {
    public static void main(String[] args) {
        int maxi = 0;
        int ones = 0;
        int[] arr = { 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1 };
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 1) {
                ones++;
                maxi = Math.max(maxi, ones);

            } else
                ones = 0;
        }
        System.out.println(maxi);
    }
}
