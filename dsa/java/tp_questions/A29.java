import java.util.*;
import java.util.Random;

public class A29{
    public static void main(String[] args)
    {   
        Scanner sc =new Scanner(System.in);
        Random rand =new Random();
        int n=rand.nextInt(100-0+1)+0;
        System.out.println(n);
        System.out.println("Guess the number under 5 attempt");
        for(int i=1;i<=5;i++)
        {
            int guess=sc.nextInt();
            if(guess==n)
                { 
                    System.out.println("you got it-");
                     break;}
            else if(guess>n) System.out.println("try less again ");
            else if(guess<n) System.out.print("try more again ");
        }


    }
}