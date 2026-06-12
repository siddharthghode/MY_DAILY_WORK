import java.util.ArrayList;

public class A03_intersection_optimised {
    public static void main(String[] args)
    {
       int[] arr1 = {1, 2, 3,3, 4, 5};
       int n1=arr1.length;
       int[] arr2 = {2, 3,3, 5, 6, 7};
       int n2=arr2.length;
        int i=0;
        int j=0;
        ArrayList<Integer> list =new ArrayList<>();
        while(i<n1 && j<n2)
        {
           if(arr1[i]==arr2[j])
           {
            list.add(arr1[i]);
            i++;
            j++;
           }
            else if(arr1[i] < arr2[j])
            {
                i++;
            }

            else
            {
                j++;
            }
        }
        System.out.println(list);
    }
}
