import java.util.Scanner;

public class Reverse_an_array{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);

        System.out.println("Enter the array Size");
        int n=sc.nextInt();

        int[] arr=new int[n];
        System.out.println("Enter the Elemets:");
        for(int g=0;g<arr.length;g++)
        {
            arr[g]=sc.nextInt();
        }

        System.out.println("Swap:");
        int i=0;
        int j=arr.length-1;
        while(i<j)
        {
           int temp=arr[i];
           arr[i]=arr[j];
           arr[j]=temp;
           i++;
           j--;
        }

        for (int k = 0; k < arr.length; k++) {
            System.out.print(" "+arr[k]);
        }
        
    }
}