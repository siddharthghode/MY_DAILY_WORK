public class A7 {
    public static void main(String[] args) {
        String a = "maddam";
        int i = 0, j = a.length() - 1;
        while (i <= j) {
            if (a.charAt(i) != a.charAt(j)) { System.out.println("Not Palindrome"); break; }
            else { i++; j--; if (i == j) System.out.println("Is Palindrome"); }
        }
    }
}
