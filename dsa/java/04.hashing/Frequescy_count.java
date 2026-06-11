import java.util.HashMap;
import java.util.Map;

public class Frequescy_count {
    public static void main(String[] args)
    {
       HashMap<Integer,Integer> map = new HashMap<>();
       int[] arr={1,2,1,4,4,4,4,7,5,5,7,0};
       for(int x:arr)
       {
        map.put(x,map.getOrDefault(x,0)+1);
       }
       System.out.println(map);
    
       int maxi_index=0;
       int maxo_element=0;
       for(Map.Entry<Integer,Integer> x : map.entrySet())
        {
            if(x.getValue() > maxi_index)
            {
                maxi_index = x.getValue();
                maxo_element = x.getKey();
            }
        }
        System.out.println("MAX ELEMENT: "+maxo_element);
        System.out.println("MAX INDEX: "+maxi_index);
    }
}
