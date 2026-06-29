import java.util.*;

public class A03_Rotate_left_by_1 {
    public static void main(String[] args)
    {
    ArrayList<Integer> arr = new ArrayList<>(Arrays.asList(1,2,3,4,5,6,7,8));
    int temp=arr.get(0);
    for(int i=1;i<=arr.size()-1;i++)
    {
        arr.set(i-1,arr.get(i));
    }
    arr.set(arr.size()-1,temp);
    System.out.println(arr);

    }
}
