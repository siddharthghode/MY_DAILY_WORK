import java.util.TreeMap;

public class Map {
    public static void main(String[] args) {
        TreeMap<Integer, String> m = new TreeMap<>();
        m.put(1, "One"); m.put(2, "Two"); m.put(3, "Three"); m.put(10, "ten"); m.put(4, "four");
        for (var e : m.entrySet()) System.out.println(e.getKey() + " " + e.getValue());
    }
}
