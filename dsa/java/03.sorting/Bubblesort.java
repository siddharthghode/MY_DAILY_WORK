import java.util.*;

public class Bubblesort{

    public static void sort(ArrayList<Integer> list,int n)
    {
       for(int i=0;i<n-1;i++)
       {
        boolean swapped=false;
        for(int j=0;j<n-i-1;j++)
        {
            if(list.get(j)>list.get(j+1))
            {
                Collections.swap(list,j,j+1);
                 swapped=true;
            }
        }
        if(!swapped) break;
       }
    }

    public static void main(String[] args)
    {
        ArrayList<Integer> list=new ArrayList<>(Arrays.asList(45,12,89,3,67,23,9,100));
        int n=list.size();
        sort(list,n);
        System.out.println(list);
    }
}