import java.util.*;

public class A14_positive_negative_arangements {

    // Static method to rearrange positives and negatives alternately
    public static int[] rearrangeBySign(int[] A) {
        List<Integer> pos = new ArrayList<>();
        List<Integer> neg = new ArrayList<>();

        // Separate positive and negative numbers
        for (int num : A) {
            if (num > 0) {
                pos.add(num);
            } else {
                neg.add(num);
            }
        }

        // Place positives at even indices and negatives at odd indices
        for (int i = 0; i < A.length / 2; i++) {
            A[2 * i] = pos.get(i);
            A[2 * i + 1] = neg.get(i);
        }

        return A;
    }

    public static void main(String[] args) {
        int[] A = { 1, 2, -4, -5 };
        int[] result = rearrangeBySign(A);
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}