import java.util.*;

public class A05_Move_all_zeros_to_the_end_optimized {
    public static void main(String[] args)
    {
        ArrayList<Integer> list = new ArrayList<>(
            Arrays.asList(1, 2, 0, 3, 0, 4, 5, 0)
        );

        int j = -1;

        // find first zero
        for(int i=0; i<list.size(); i++)
        {
            if(list.get(i)==0)
            {
                j=i;
                break;
            }
        }

        if(j==-1) return;
;

        // move zeros
        for(int k=j+1; k<list.size(); k++)
        {
            if(list.get(k)!=0)
            {
                Collections.swap(list,j,k);
                j++;
            }
        }


        System.out.println(list);
    }
}