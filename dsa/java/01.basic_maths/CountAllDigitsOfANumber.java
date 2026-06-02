public class CountAllDigitsOfANumber {
    public static void main(String[] args) {
        int a = 55555;
        int count = 0, lastDigit = 0;
        while (a > 0) {
            lastDigit = a % 10;
            count++;
            a /= 10;
        }
        System.out.println(count);
        System.out.println(lastDigit);
    }
}
