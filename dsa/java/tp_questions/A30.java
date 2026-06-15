import java.util.*;

public class A30 {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 5, 6, 7, 8 };
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            if (arr[i] == arr[i + 1] - 1) {
                System.out.println("no");
            } else if (arr[i] != arr[i + 1] - 1) {
                System.out.println(arr[i + 1] - 1 + ":: is the missing number");
                break;
            }
        }

    }
}
