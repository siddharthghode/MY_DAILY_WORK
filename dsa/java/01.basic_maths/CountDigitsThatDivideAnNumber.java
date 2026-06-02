public class CountDigitsThatDivideAnNumber {
    static int countDigits(int num) {
        int count = 0, copy = num;
        while (num > 0) {
            int digit = num % 10;
            num /= 10;
            if (digit != 0 && copy % digit == 0) count++;
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(countDigits(1248));
    }
}
