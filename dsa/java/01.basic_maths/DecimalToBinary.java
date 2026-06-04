// import java.util.*;

public class DecimalToBinary {
    public static void main(String[] args) {
        int decimal=1234;
        int binary=0;
        int place=1;
        while(decimal>0)
        {
            int remainder=decimal%2;
            binary=binary+remainder*place;
            place=place*10;
            decimal=decimal/2;
        }
        System.out.println(binary);
    }
}