import java.util.Scanner;
public class Factorial {
 public static void main(String[] args)
 {
       Scanner sc = new Scanner(System.in);
       System.out.println("Enter the number for factorial");
       int n=sc.nextInt();
       int sum=1;
       for(int i=1;i<=n;i++)
       {
          sum+=sum*i;
       }
       System.out.print("The factorial of an number is::"+sum);
 }   
}
