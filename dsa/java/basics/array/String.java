import java.util.Scanner;

public class String {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        java.lang.String a = sc.nextLine();
        System.out.println("String: " + a);
        System.out.println("Third elements: " + a.charAt(2));
        System.out.println("All elements:");
        for (int i = 0; i < a.length(); i++) System.out.println(i + ":" + a.charAt(i));
    }
}
