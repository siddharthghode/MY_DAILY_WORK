import java.util.*;

public class Findmaxi {
       public static void main(String[] args)
       {
          ArrayList<Integer> List = new ArrayList<>(Arrays.asList(10,20,0,100,6));
           int maxi=0;
           for(int i=0;i<List.size()-1;i++)
           {
             if(List.get(i)>List.get(maxi))
             {
                maxi=i;
             }
        }
        System.out.println(List.get(maxi));
       }
}
