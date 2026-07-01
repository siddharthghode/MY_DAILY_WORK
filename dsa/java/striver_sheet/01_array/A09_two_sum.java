import java.util.HashMap;

public class A09_two_sum {

    public static void twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> mpp = new HashMap<>();
        for (int i = 0; i <= nums.length; i++) {
            int need = target - nums[i];
            if (mpp.containsKey(need)) {
                int other = mpp.get(need);
                System.out.println(other + " " + i);
                return;
            }
            mpp.put(nums[i], i);
        }
        System.out.println("no target pair found");

    }

    public static void main(String args[]) {
        int[] nums = { 1, 6, 2, 10, 3 };
        int target = 7;
        twoSum(nums, target);
    }
}
