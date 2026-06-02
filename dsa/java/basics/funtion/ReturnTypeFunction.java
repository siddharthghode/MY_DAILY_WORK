public class ReturnTypeFunction {
    static int sum(int a, int b) {
        System.out.print("The sum of " + a + " and " + b + " is: ");
        return a + b;
    }

    public static void main(String[] args) {
        int newsum = sum(4, 5);
        System.out.println(newsum);
    }
}
