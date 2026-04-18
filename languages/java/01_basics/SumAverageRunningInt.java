import java.util.Scanner;

public class SumAverageRunningInt{
    public static void main(String[] args){
    int sum=0;
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the numebers initial a and final b ");
    int a=sc.nextInt();
    int b=sc.nextInt();
    // for(int i=a;i<=b;i++)
    // {
    //   sum=sum+i;
    // }
    // hile(a<=b)
    // 
//    sum=sum+a;
//    a++;
    // 
    while(a<=b)
    {
        sum=sum+(a*a);
        a++;
    }
    System.out.println("The sum is:"+sum);
    }
}