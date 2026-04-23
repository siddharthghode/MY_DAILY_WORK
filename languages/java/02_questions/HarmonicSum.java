import java.util.Scanner;
public class HarmonicSum{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the value of n:");
        double n = sc.nextInt();
     double sumLTR=0.0;
     double sumRTL=0.0;
     double difference;
        for(int i=1; i<=n; i++)
        {
            sumLTR += 1.0/i;
        }
        for(double i=n; i>=1; i--)
        {
            sumRTL += 1.0/i;
        }
        difference= sumLTR-sumRTL;
        System.out.println("The harmonic sum is: " + sumLTR);
        System.out.println("the sum form RTL is ::"+sumRTL);
        System.out.println("the diffrence is--"+difference);
    }
}