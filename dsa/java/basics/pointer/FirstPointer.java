public class FirstPointer {
    public static void main(String[] args) {
        int x = 10;
        // Java has no pointers; references work similarly
        // Printing the identity hash code as a proxy for address
        int[] y = {x};
        System.out.println(System.identityHashCode(y));
    }
}
