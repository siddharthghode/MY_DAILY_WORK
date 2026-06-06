import java.util.*;
public class Palindrome {
   static boolean checkpal(String a,int i,int end) 
{
    while(i<=end)
{
    if(a.charAt(i)!=a.charAt(end)) return false;

      i++;
      end--;
} return true;
}
public  static void main(String[] args)
{
Scanner sc = new Scanner(System.in);
System.out.println("Enter the word:");
String a=sc.next();
System.out.println(checkpal(a,0,a.length()-1));
}
}
