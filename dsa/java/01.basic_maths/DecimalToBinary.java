import java.util.ArrayList;
import java.util.Collections;

public class DecimalToBinary {
    public static void main(String[] args) {
        int dnum = 10;
        ArrayList<Integer> bnum = new ArrayList<>();
        while (dnum > 0) { bnum.add(dnum % 2); dnum /= 2; }
        Collections.reverse(bnum);
        for (int b : bnum) System.out.print(b);
    }
}
