public class MinMaxInArray {
    public static void main(String[] args) {
        int[] a = {3, 5, 7, 2, 8, 6, 4, 1};
        int max = a[0], min = a[0];
        for (int x : a) { if (x > max) max = x; if (x < min) min = x; }
        System.out.println("max" + max);
        System.out.println("min" + min);
    }
}
