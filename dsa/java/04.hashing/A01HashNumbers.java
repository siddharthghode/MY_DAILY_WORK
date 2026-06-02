import java.util.Scanner;

public class A01HashNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        int[] hash = new int[1000000];
        for (int x : arr) hash[x]++;

        int q = sc.nextInt();
        while (q-- > 0) {
            int number = sc.nextInt();
            System.out.println("times: " + hash[number]);
        }
    }
}
