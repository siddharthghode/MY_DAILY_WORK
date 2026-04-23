import java.util.*;
import java.util.Scanner;

public class Bubblesort{

    public static void bubblesort(int[] arr,int n)
    {
        for(int i=0;i<n;i++)
        {      
            boolean flag=true;
            for(int j=i+1;j<=n-i-1;j++)
                {
                    if(arr[i]>arr[j])
                    {
                        int temp=arr[i];
                        arr[i]=arr[j];
                        arr[j]=temp;
                    } flag=false;

                }
        if(!flag)
            {
                break;
            }    
        
            }
    }
    public static void main(String[] args)
    {
       int arr[]={5,1,4,2,8};
       int n=arr.length;
    //    Bubblesort obj=new Bubblesort();
    //    obj.bubblesort(arr, n);
    bubblesort(arr, n);
       for(int i=0;i<n;i++)
       {
       System.out.println(arr[i]+" ");
       }
    }
}