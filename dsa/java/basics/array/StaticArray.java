public class StaticArray {
    public static void main(String[] args) {
        int[] arr = {10, 20, 31, 40, 50};
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % 2 == 0) { System.out.println("Position" + i + ":" + arr[i]); count++; }
        }
        if (count == 0) System.out.println("no even elements found");
    }
}
