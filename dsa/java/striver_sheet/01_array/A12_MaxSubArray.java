import java.util.*;

public class A12_MaxSubArray {
    public static long count_max(int[] nums) {
        long maxi = Long.MIN_VALUE;
        long sum = 0;

        for (int i = 0; i < nums.length; i++) {

            sum += nums[i];

            if (sum > maxi) {
                maxi = sum;
            }

            if (sum < 0) {
                sum = 0;
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        int[] arr = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
        System.out.println("The maximum subarray sum is: " + count_max(arr));
    }
}
