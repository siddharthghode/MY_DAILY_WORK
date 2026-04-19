import java.util.Scanner;

public class Scanner_input_05{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number a:");
        int num= sc.nextInt();
        // sc.nextLine();
        System.out.println("The entered numebr is:"+num);
        System.out.println("Enter a char:");
        char a=sc.next().charAt(0);
        System.out.println("the string user given is:"+a);
    }
}