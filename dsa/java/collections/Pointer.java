public class Pointer {
    public static void main(String[] args) {
        int x = 10;
        // Java has no pointers; use identityHashCode as proxy for address
        System.out.println(System.identityHashCode(Integer.valueOf(x)));
    }
}
