import java.lang.reflect.Array;
import java.util.*;

public class A02_Remove_dublicates{
    static void remove_dub(ArrayList<Integer> list)
    {
        int i=0;
        for(int j=1;j<=list.size()-1;j++)
        {
            if(list.get(i)!=list.get(j))
            {
                i++;
                list.set(i,list.get(j));
            }
        }
        int k=i+1;
        while(k<=list.size()-1)
        {
           list.remove(k);
           i++;
        }
    }
    public static void main(String[] args)
    {
        System.out.println("Enter the number of elements for array");
        Scanner sc = new Scanner(System.in);

        int n=sc.nextInt();
        ArrayList<Integer> list = new ArrayList<>();
        for(int i=0;i<n;i++)
        {
            int value=sc.nextInt();
            list.add(value);
        }
        System.out.println(list);
        Collections.sort(list);
        System.out.println(list);
        sc.close();
        remove_dub(list);
        System.out.println(list);
    }
}