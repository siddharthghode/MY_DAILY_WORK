import java.util.*;

public class A08_find_the_longest_subarray_with_sum_k {

    public static void main(String[] args) {
        // works for positive/negative numbers its better silution
        // int[] arr = { 2, 1, 3, 2, 4, 1, 1, 5, 2, 3, 1 };
        // int k = 7;
        // HashMap<Integer, Integer> presum = new HashMap<>();
        // int sum = 0;
        // int max_len = 0;
        // for (int i = 0; i < arr.length; i++) {
        // sum += arr[i];
        // if (!presum.containsKey(sum)) {
        // presum.put(sum, i);
        // }
        // if (sum == k) {
        // max_len = Math.max(max_len, i + 1);
        // }

        // int remaining = sum - k;
        // if (presum.containsKey(remaining)) {
        // max_len = Math.max(max_len, i - presum.get(remaining));
        // }

        // }
        // System.out.println(max_len);

        //// works only for positive/zeros numbers and optimised
        int[] arr = { 2, 1, 3, 2, 4, 1, 1, 1, 5, 2, 3, 1 };
        int k = 8;
        int max_len = 0;
        int sum = 0;
        int right = 0;
        int left = 0;
        while (right < arr.length) {
            sum += arr[right];
            while (left <= right && sum > k) {
                sum -= arr[left];
                left++;
            }
            if (sum == k) {
                max_len = Math.max(max_len, right - left + 1);
            }
            right++;
        }
        System.out.println(max_len);
    }
}