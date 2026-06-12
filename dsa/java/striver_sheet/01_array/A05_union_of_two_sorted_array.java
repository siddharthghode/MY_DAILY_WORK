import java.util.Arrays;
import java.util.TreeSet;

public class A05_union_of_two_sorted_array {
    public static void main(String[] args)
    {
        int[] arr1 = {1, 2, 3, 4, 5};
        int[] arr2 = {2, 3, 5, 6, 7};
        TreeSet<Integer> set=new TreeSet<>();
        for(int i=0;i<=arr1.length-1;i++)
        {
           set.add(arr1[i]);
        }
        for(int j=0;j<=arr2.length-1;j++)
        {
           set.add(arr2[j]);
        }
        for(int x:set)
        {
            System.out.println(x);
        }
    }
}
