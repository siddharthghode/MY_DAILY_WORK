import java.util.Map;
import java.util.TreeMap;

public class A03HashIntUsingMap {
    public static void main(String[] args) {
        int[] arr = {1, 2, 2, 1, 9};
        Map<Integer, Integer> p = new TreeMap<>();
        for (int x : arr) p.merge(x, 1, Integer::sum);
        for (Map.Entry<Integer, Integer> e : p.entrySet())
            System.out.println(e.getKey() + "->" + e.getValue());
    }
}
