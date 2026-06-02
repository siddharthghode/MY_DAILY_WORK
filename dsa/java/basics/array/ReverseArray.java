public class ReverseArray {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int start = 0, end = arr.length - 1;
        while (start < end) {
            int tmp = arr[start]; arr[start] = arr[end]; arr[end] = tmp;
            start++; end--;
        }
        for (int x : arr) System.out.print(x + " ");
    }
}
