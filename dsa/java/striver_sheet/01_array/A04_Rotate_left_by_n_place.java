import java.util.ArrayList;
import java.util.Arrays;

public class A04_Rotate_left_by_n_place {
    public static void main(String[] args)
    {
         ArrayList<Integer> arr = new ArrayList<>(Arrays.asList(1,2,3,4,5,6,7,8));
         int rotate=7;
         int d=rotate%arr.size();
         ArrayList<Integer> temp=new ArrayList<>();
         // add elements into temp
         for(int i=0;i<d;i++)
         {
            temp.add(i,arr.get(i));
         }
         //shift the elements
         for(int j=d;j<arr.size();j++)
         {
                arr.set(j-d,arr.get(j));
         }
         //set elements to the back
         for(int k=0;k<d;k++)
         {
            arr.set(arr.size()-d+k, temp.get(k));
         }
         for(int x:arr)
         {
            System.out.println(x);
         }
        
    }
}
