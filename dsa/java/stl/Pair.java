import java.util.AbstractMap.SimpleEntry;

public class Pair {
    public static void main(String[] args) {
        SimpleEntry<Integer, Integer> p = new SimpleEntry<>(1, 2);
        System.out.println(p.getKey() + " " + p.getValue());

        // nested pair simulation
        SimpleEntry<SimpleEntry<Integer, Integer>, Integer> p1 = new SimpleEntry<>(new SimpleEntry<>(2, 5), 6);
        System.out.println(p1.getKey().getKey() + " " + p1.getKey().getValue() + " " + p1.getValue());

        // array of pairs
        SimpleEntry<Integer, Integer>[] arr = new SimpleEntry[]{
            new SimpleEntry<>(1, 3), new SimpleEntry<>(3, 4), new SimpleEntry<>(4, 5)
        };
        System.out.println(arr[1].getValue());
    }
}
