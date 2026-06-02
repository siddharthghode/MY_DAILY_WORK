import java.util.Scanner;

public class A02HashChar {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String s = sc.next();

        int[] hash = new int[256];
        for (char ch : s.toCharArray()) hash[ch]++;

        System.out.print("How many queries do you want? ");
        int q = sc.nextInt();
        while (q-- > 0) {
            System.out.print("Enter character to check frequency: ");
            char c = sc.next().charAt(0);
            System.out.println("Frequency of '" + c + "' is: " + hash[c]);
        }
    }
}
