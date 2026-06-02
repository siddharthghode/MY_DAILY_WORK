public class GetDigits {
    public static void main(String[] args) {
        int number = 12345;
        int getLastNumber = number % 10;
        System.out.println(getLastNumber + " now number is: " + number);
        int removeLastNumber = number / 10;
        System.out.println(removeLastNumber);
    }
}
