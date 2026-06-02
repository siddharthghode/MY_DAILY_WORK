public class Pattern09 {
    static void star1(int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) System.out.print(" ");
            for (int j = 0; j < 2 * i + 1; j++) System.out.print("*");
            System.out.println();
        }
    }

    static void star2(int n) {
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j < i; j++) System.out.print(" ");
            for (int j = 0; j < 2 * n - (2 * i + 1); j++) System.out.print("*");
            System.out.println();
        }
    }

    public static void main(String[] args) { star1(5); star2(5); }
}
