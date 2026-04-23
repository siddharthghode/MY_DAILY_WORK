import java.util.*;
import java.util.Scanner;

public class Selectionsort{

    static void selectionsort(int[] arr,int n)
    {
        for(int i=0;i<=n-1;i++)
        {    int min_value=i;
            for(int j=i+1;j<=n-1;j++)
            {
              if(arr[j]<arr[min_value])
              min_value=j;
            }
            int temp=arr[i];
            arr[i]=arr[min_value];
            arr[min_value]=temp;
        }
    }
    public static void main(String[] args)
    {
      int arr[]={5,1,4,2,8};
        int n=arr.length;
        selectionsort(arr, n);
       for(int i=0;i<n;i++)
       {
       System.out.println(arr[i]+" ");
       }
    }
}