public class Armstrong {
    public static void main(String[] args) {
        int n = 153, copyN = n, sum = 0, count = 0;
        int tmp = n;
        while (tmp > 0) { count++; tmp /= 10; }
        tmp = copyN;
        while (tmp > 0) {
            int digit = tmp % 10;
            sum += (int) Math.pow(digit, count);
            tmp /= 10;
        }
        System.out.println(sum == copyN ? "yes it is armstrong" : "it is not armstrong");
    }
}
