import java.util.Arrays;
import java.util.HashSet;

public class A16_longest_consecutive_sequence {

    // brute force
    public static void find_consi(int[] arr) {
        int n = arr.length;
        int longest = 1;
        for (int i = 0; i < n; i++) {
            int x = arr[i];
            int cnt = 1;
            while (true) {
                boolean found = false;
                for (int j = 0; j < n; j++) {
                    if (arr[j] == x + 1) {
                        cnt++;
                        x = x + 1;
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    break;
                }
            }
            longest = Math.max(cnt, longest);
        }
        System.out.println(longest);
    }

    // better
    public static void find_consi_better(int[] arr) {
        Arrays.sort(arr);
        int n = arr.length;
        int cnt = 0;
        int length = 1;
        int x = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            if (arr[i] == x + 1) {
                cnt++;
                x = arr[i];
            } else if (arr[i] != x) {
                x = arr[i];
                cnt = 0;
            }
            length = Math.max(cnt, length);
        }
        System.out.println(length);
    }

    // optimal approch
    public static void find_consi_optimal(int[] arr) {
        int n = arr.length;
        int longest = 1;
        if (n == 0) {
            System.out.println("no sequence");
            return;
        }

        HashSet<Integer> hsh = new HashSet<>();
        for (int i = 0; i < n; i++) {
            hsh.add(arr[i]);
        }
        for (int x : hsh) {
            if (!hsh.contains(x - 1)) {
                int num = x;
                int cnt = 1;
                while (hsh.contains(num + 1)) {
                    num = num + 1;
                    cnt++;
                }
                longest = Math.max(longest, cnt);
            }
        }
        System.out.println("longest:" + longest);
    }

    public static void main(String args[]) {
        int[] arr = { 102, 4, 100, 1, 101, 3, 2, 1, 1 };
        // int[] arr = {};
        // find_consi(arr);
        // find_consi_better(arr);
        find_consi_optimal(arr);
    }

}
