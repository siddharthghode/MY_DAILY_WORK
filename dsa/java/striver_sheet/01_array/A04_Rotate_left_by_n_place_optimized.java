import java.util.*;
public class A04_Rotate_left_by_n_place_optimized{
    static public void main(String[] args)
    {
         ArrayList<Integer> arr = new ArrayList<>(Arrays.asList(1,2,3,4,5,6,7,8));
          int rotate=2;
        int d=rotate%arr.size();
          Collections.reverse(arr.subList(0, d));
          Collections.reverse(arr.subList(d,arr.size()));
          Collections.reverse(arr);
          for(int x:arr)
          {
            System.out.print(" "+x);
          }
       
    }
}
