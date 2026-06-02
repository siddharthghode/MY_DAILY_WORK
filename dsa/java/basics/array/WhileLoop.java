import java.util.Scanner;

public class WhileLoop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        java.lang.String a = sc.nextLine();
        System.out.println("String: " + a);
        System.out.println("Third elements: " + a.charAt(2));
        System.out.println("All elements:");
        int i = 0;
        while (i < a.length()) { System.out.println(i + ":" + a.charAt(i)); i++; }
    }
}
