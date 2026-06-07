import java.util.*;

public class Reverselist{
    public static void main(String[] args)
    {
        ArrayList<Integer> list = new ArrayList<>(Arrays.asList(10,20,30,400));
        int i=0;
        int j=list.size()-1;
        while (i<=j) {
            Collections.swap(list, i, j); 
            i++;
            j--;
        }
          System.out.println(list);
    }
}