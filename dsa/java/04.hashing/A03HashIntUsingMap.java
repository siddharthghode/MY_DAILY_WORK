import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

public class A03HashIntUsingMap {
    public static void main(String[] args) {
       int[] arr={1,2,1,2,1,2,6,6,4,3,9,9,10};
       int n=arr.length;
       HashMap<Integer,Integer> hash= new HashMap<>();
       for(int i=0;i<n;i++)
       {
        if(hash.containsKey(arr[i])) {
                hash.put(arr[i], hash.get(arr[i]) + 1);
            }
            else {
                hash.put(arr[i], 1);
            }
       }
       System.out.println(hash);
    }
}
