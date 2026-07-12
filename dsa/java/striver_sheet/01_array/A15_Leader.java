import java.util.ArrayList;

public class A15_Leader {

    public static void get_leaders(int[] arr, int n) {
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            boolean leader = true;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] > arr[i]) {
                    leader = false;
                    break;
                }
            }
            if (leader == true)
                list.add(arr[i]);
        }
        System.out.println(list);
    }

    public static void main(String args[]) {
        int[] arr = { 16, 17, 4, 3, 5, 2 };
        int n = arr.length;
        get_leaders(arr, n);
    }
}
