import java.util.Scanner;

public class ArrayInputOutput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the number of array you want to create");
        int n = sc.nextInt();
        int[] a = new int[n];
        System.out.println("enter " + n + " elements");
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        System.out.println("the elements in array are:");
        for (int x : a) System.out.print(x + " ");
    }
}
