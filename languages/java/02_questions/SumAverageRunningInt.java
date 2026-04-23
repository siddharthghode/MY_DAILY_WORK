import java.util.*;
import java.util.Scanner;
import java.util.concurrent.CountDownLatch;

public class SumAverageRunningInt{
    public static void main(String args[]){
       Scanner sc =new Scanner(System.in);
         System.out.println("Enter the UPPERBOUND and LOWERBOUND");
            int upperBound = sc.nextInt();
            int LOWERBOUND= sc.nextInt();
            int sum=0;
            int count=0;
            float average;
            for(int i=LOWERBOUND;i<=upperBound;i++){
                sum+=i;
                ++count;
            }
            average=(float)sum/count;
            System.out.println("The sum is: "+sum);
            System.out.println("Count:"+count);
            System.out.println("The average is:"+average);
    }
}