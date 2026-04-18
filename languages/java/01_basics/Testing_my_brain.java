import java.util.Scanner;

public class Testing_my_brain{
    public static void main(String[] args)
    {
       Scanner sc = new Scanner(System.in);
       System.out.println("Enetr the number");
       int num=sc.nextInt();
       System.out.println("The num is:"+num);
       System.out.println("Enter the char:");
       char na=sc.next().charAt(0);
       System.out.println("The Char:"+na);
       System.out.println("Enetr the line");
       String full=sc.nextLine();
       System.out.println("The Line is"+full);
    }
}
