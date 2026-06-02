public class FunctionCallByValue {
    static int changeNumber(int a) {
        a = 100;
        return a;
    }

    public static void main(String[] args) {
        int a = 10;
        System.out.println("Before changing the number: " + a);
        int newNumber = changeNumber(a);
        System.out.println("After changing the number: " + a);
        System.out.println("The new number is: " + newNumber);
    }
}
