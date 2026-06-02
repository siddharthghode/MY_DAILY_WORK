public class FunctionCallByRefrence {
    static int changeNumber(int[] a) {
        a[0] = 100;
        return a[0];
    }

    public static void main(String[] args) {
        int[] a = {10};
        System.out.println("Before changing the number: " + a[0]);
        int newNumber = changeNumber(a);
        System.out.println("After changing the number: " + a[0]);
        System.out.println("The new number is: " + newNumber);
    }
}
