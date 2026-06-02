import java.util.Arrays;

public class AllOperationsToArray {
    public static void main(String[] args) {
        int[] a = {0, 1};
        for (int i = 0; i < a.length - 1; i++)
            if (a[i] == a[i + 1]) { a[i] *= 2; a[i + 1] = 0; }

        int[] ans = new int[a.length];
        int idx = 0;
        for (int x : a) if (x != 0) ans[idx++] = x;
        for (int x : ans) System.out.print(x + " ");
    }
}
