import java.util.ArrayList;
import java.util.Arrays;
import java.util.*;

public class Insertionsort{
    static void sort(ArrayList<Integer> list,int n)
    {
      for(int i=1;i<n;i++)
      {
        int j=i;
        while(j>0 && list.get(j-1)>list.get(j))
        {
          Collections.swap(list,j-1,j);
          j--;
        }
      }
    }
    public static void main(String[] args)
    {
     ArrayList<Integer> list=new ArrayList<>(Arrays.asList(45,12,89,3,67,23,9,100));
     int n=list.size();
     sort(list,n);
     for(int x:list)
     {
      System.out.println(x);
     }
    }
}