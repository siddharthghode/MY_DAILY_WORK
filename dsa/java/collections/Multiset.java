import java.util.TreeMap;

public class Multiset {
    public static void main(String[] args) {
        TreeMap<Integer, Integer> mset = new TreeMap<>();
        for (int x : new int[]{4, 4, 5}) mset.merge(x, 1, Integer::sum);
        for (var e : mset.entrySet())
            for (int i = 0; i < e.getValue(); i++) System.out.print(e.getKey() + " ");
    }
}
