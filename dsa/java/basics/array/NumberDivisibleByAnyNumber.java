public class NumberDivisibleByAnyNumber {
    public static void main(String[] args) {
        int[] a = {10, 15, 23, 30, 42, 55, 60, 75, 80, 91};
        int count = 0;
        for (int x : a) if (x % 3 == 0 && x % 5 == 0) count++;
        System.out.println("Number of elements divisible by both 3 and 5: " + count);
    }
}
