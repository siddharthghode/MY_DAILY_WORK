public class CountEven {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 6};
        int count = 0;
        for (int x : arr) if (x % 2 == 0) count++;
        System.out.println("Number of even elements: " + count);
    }
}
