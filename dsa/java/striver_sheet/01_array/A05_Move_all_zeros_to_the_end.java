import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class A05_Move_all_zeros_to_the_end {
    public static void main(String[] args)
    {
        ArrayList<Integer> arr= new ArrayList<>(Arrays.asList(1,2,0,31,0,1,6,3,0,7,4,0));
        ArrayList<Integer> temp= new ArrayList<>();
        for(int i=0;i<=arr.size()-1;i++)
        {
            if(arr.get(i)!=0)
            {
                temp.add(arr.get(i));
            }
        }
        

        while(arr.size()>temp.size())
        {
          temp.add(0);
        }

        for(int x:temp)
        {
            System.out.print(" "+x);
        }

    }
    
}
