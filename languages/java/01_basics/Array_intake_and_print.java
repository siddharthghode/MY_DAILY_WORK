import java.util.Scanner;

public class Array_intake_and_print  {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Size of Aaray");
        int n=sc.nextInt();
        int[] arr = new int[n];

        System.out.println("Enter the array:");

        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
       
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
}