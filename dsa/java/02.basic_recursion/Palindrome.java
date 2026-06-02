public class Palindrome {
    static boolean checkPalindrome(String word, int i, int end) {
        if (i >= end) return true;
        if (word.charAt(i) != word.charAt(end)) return false;
        return checkPalindrome(word, i + 1, end - 1);
    }

    public static void main(String[] args) {
        String word = "madam";
        System.out.println(checkPalindrome(word, 0, word.length() - 1) ? "Palindrome" : "Not Palindrome");
    }
}
