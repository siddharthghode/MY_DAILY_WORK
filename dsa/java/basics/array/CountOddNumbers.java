public class CountOddNumbers {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 6};
        int odd = 0;
        for (int x : arr) if (x % 2 != 0) System.out.print("  " + odd++);
        System.out.println(odd);
    }
}
