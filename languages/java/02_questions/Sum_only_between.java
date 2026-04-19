import java.util.Scanner;
public class Sum_only_between{
    public static void main(String[] args) {
     Scanner sc = new Scanner(System.in);

   System.out.println("Enter the numbers to do sum:");
   int a =sc.nextInt();
   long b=sc.nextInt();
       
    int sum_in_between=0;
    int count=0;
    int sum =0;
    int count_for_non_between_numbers=0;
    for (int i=a;i<=b;i++)
    {
        if(i>=100 && i<=8899){
            sum_in_between=sum_in_between+i;
            count++;
        }
        else{
            sum=sum+i;
            count_for_non_between_numbers++;
        }
    }
    System.out.println("The sums between(100-8899):"+sum_in_between+" and other:"+count_for_non_between_numbers); 
    
}
}