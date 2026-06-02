public class A8 {
    public static void main(String[] args) {
        int[] a = {1, 5, 3, 9, 5, 2, 5, 6};
        int max = a[0], second = Integer.MIN_VALUE;
        for (int x : a) if (x > max) max = x;
        for (int x : a) if (x > second && x != max) second = x;
        System.out.println(second);
    }
}
