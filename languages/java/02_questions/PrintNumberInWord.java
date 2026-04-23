import java.util.*;
import java.util.Scanner;

public class PrintNumberInWord{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number between 0 and 9: ");
        int number = scanner.nextInt();
        if(number==1){
        System.out.println("ONE");
          }
          else if(number==2){
              System.out.println("TWO");
          }
          else if(number==3){
              System.out.println("THREE");
          }
          else if(number==4){
              System.out.println("FOUR");
          }
          else if(number==5){
              System.out.println("FIVE");
          }
          else if(number==6){
              System.out.println("SIX");
          }
          else if(number==7){
              System.out.println("SEVEN");
          }
          else if(number==8){
              System.out.println("EIGHT");
          }
          else if(number==9){
              System.out.println("NINE");
          }
          else
          {
              System.out.println("OTHER");
          }
    }
}