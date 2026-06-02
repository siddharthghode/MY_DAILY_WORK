public class BinaryToDecimal {
    public static void main(String[] args) {
        int bnum = 1011, dnum = 0, i = 0;
        while (bnum > 0) {
            int last = bnum % 10;
            dnum += last * (int) Math.pow(2, i);
            bnum /= 10;
            i++;
        }
        System.out.println("the decimal number is: " + dnum);
    }
}
