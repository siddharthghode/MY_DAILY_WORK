import java.util.Scanner;

public class Factorial{
    public static void main(String[] args)
    {
       Scanner sc = new Scanner(System.in);
       System.out.print("Enter the Factorial number:");
       int a = sc.nextInt();
       sc.nextLine();
       System.out.print("Enter some timepass LINE about yourself:");
       String b = sc.nextLine();
       System.out.println("you enter:"+b);
       int fact = 1;
       do{
        fact = fact * a;
        a--;
       }while(a>0);
       System.out.println("The Factorial is: " + fact);
    }
}