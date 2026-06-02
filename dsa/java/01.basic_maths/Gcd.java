public class Gcd {
    static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public static void main(String[] args) {
        int n1 = 20, n2 = 30;
        System.out.println("GCD: " + gcd(n1, n2));
    }
}
