import java.util.TreeSet;

public class Set {
    public static void main(String[] args) {
        TreeSet<Integer> s = new TreeSet<>();
        s.add(1); s.add(4); s.add(6); s.add(1); s.add(10);
        if (s.contains(6)) System.out.println("present");
    }
}
