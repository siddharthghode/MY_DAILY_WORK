import java.util.*;

public class A01_Findlargest {
    public static void main(String[] args)
    {
         int[] arr={1,2,3,4,5,6,7};
         int maxi=-1;
         for(int i=0;i<=arr.length-1;i++)
         {
            if(arr[i]>maxi)
            {
                 maxi=i;
            }
         }
         System.out.println("Largest_elemnet is : "+arr[maxi]);


         
    }
}
