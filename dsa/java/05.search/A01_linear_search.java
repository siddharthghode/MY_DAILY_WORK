import java.util.*;
public class A01_linear_search{

    public static void main(String[] args)
    {
        int[] arr={1,4,1,7,4,3,9,3,22,557,2,9,7,2,1,4,6};
        int num=3;
        for(int i=0;i<=arr.length-1;i++)
        {
                if(arr[i]==num)
                {
                    System.out.println(num+" is on "+(i+1)+" place");
                    break;
                }
        }
    }
}