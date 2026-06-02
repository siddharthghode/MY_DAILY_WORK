import java.util.Scanner;

public class A1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("is student present or not");
        boolean present = sc.nextBoolean();
        System.out.println(present ? "0" : "1");
    }
}
