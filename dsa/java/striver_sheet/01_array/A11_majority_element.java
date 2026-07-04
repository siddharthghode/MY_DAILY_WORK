import java.util.*;

public class A11_majority_element {

    public static void get_max_better(int[] nums, int n) {
        HashMap<Integer, Integer> mpp = new HashMap<>();
        // Store frequency of each element
        for (int i = 0; i < n; i++) {
            mpp.put(nums[i], mpp.getOrDefault(nums[i], 0) + 1);
        }
        // Find the majority element
        for (int i = 0; i < n; i++) {
            if (mpp.get(nums[i]) > n / 2)
                System.out.println(nums[i]);
            break;
        }
    }

    public static void get_max_optimal(int[] nums, int n) {
        int cnt = 0;
        int ele = 0;
        for (int i = 0; i < n; i++) {
            if (cnt == 0) {
                cnt = 1;
                ele = nums[i];
            } else if (nums[i] == ele) {
                cnt++;
            } else {
                cnt--;
            }
        }
        System.out.println(ele);
    }

    public static void main(String[] args) {

        int[] nums = { 7, 0, 0, 1, 7, 7, 2, 7, 7 };

        int n = nums.length;
        // get_max_better(nums, n);
        get_max_optimal(nums, n);

    }
}
