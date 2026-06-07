import java.util.Scanner;

public class IntakeandPrintArray {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of array you want to input::");
        int n=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++)
        {
            arr[i]=sc.nextInt();
        }
        System.out.println("The entered arrays are:");
        for(int i=0;i<=n;i++)
        {
            System.out.println(arr[i]);
        }
    }
}
