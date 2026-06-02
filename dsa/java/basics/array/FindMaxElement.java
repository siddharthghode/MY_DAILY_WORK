public class FindMaxElement {
    public static void main(String[] args) {
        int[] array = {10, 20, 30, 40, 50, 60};
        int max = array[0];
        for (int x : array) if (x > max) max = x;
        System.out.println("max =" + max);
    }
}
