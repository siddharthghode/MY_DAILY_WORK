public class A31 {
    public static void main(String[] args) {
        int n = 204000;
        long sum = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 2 != 0) {
                sum += Math.pow(i, 2);
            }
        }
        System.out.println(sum);
    }
}
