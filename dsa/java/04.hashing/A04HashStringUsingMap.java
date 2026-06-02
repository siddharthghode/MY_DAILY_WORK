import java.util.Map;
import java.util.TreeMap;

public class A04HashStringUsingMap {
    public static void main(String[] args) {
        Map<Character, Integer> a = new TreeMap<>();
        String s = "hellowOrld";
        for (char ch : s.toCharArray()) a.merge(ch, 1, Integer::sum);
        for (Map.Entry<Character, Integer> e : a.entrySet())
            System.out.println(e.getKey() + " -> " + e.getValue());
    }
}
