import java.util.*;

public class Printlist {
    public static void main(String[] args)
    {
        ArrayList<Integer> List = new ArrayList<>(Arrays.asList(10,20,30,40));
        for(int i=0;i<List.size()-1;i++)
        {System.out.println(List.get(i));}
    }
}
