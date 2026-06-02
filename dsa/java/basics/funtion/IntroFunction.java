import java.util.Scanner;

public class IntroFunction {
    static int add(int a, int b) { return a + b; }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("input a: and b:");
        int a = sc.nextInt(), b = sc.nextInt();
        System.out.println("The add is" + add(a, b));
    }
}
