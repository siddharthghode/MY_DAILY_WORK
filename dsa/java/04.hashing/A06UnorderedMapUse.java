import java.util.HashMap;
import java.util.Map;

public class A06UnorderedMapUse {
    public static void main(String[] args) {
        Map<Character, Integer> a = new HashMap<>();
        String s = "hellowOrld";
        for (char ch : s.toCharArray()) a.merge(ch, 1, Integer::sum);
        for (Map.Entry<Character, Integer> e : a.entrySet())
            System.out.println(e.getKey() + " -> " + e.getValue());
    }
}
