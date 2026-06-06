import java.util.*;

public class Bubblesort{

    public static void sort(int[] array,int n)
    {
       for(int i=0;i<n-1;i++)
       {
        for(int j=0;j<n-i-1;j++)
        {
            if(array[j]>array[j+1])
            {
                int temp=array[j];
                array[j]=array[j+1];
                array[j+1]=temp;
            }
        }
       }
    }

    public static void main(String[] args)
    {
        int[] array={45,12,89,3,67,23,9,100};
        int n=array.length;
        sort(array,n);
        for(int i=0;i<n-1;i++)
        {
            System.out.println(array[i]);
        }
    }
}