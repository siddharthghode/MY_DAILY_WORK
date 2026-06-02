import java.util.Map;
import java.util.TreeMap;

public class A05HighestAndLowestElement {
    public static void main(String[] args) {
        int[] arr = {1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6};
        Map<Integer, Integer> p = new TreeMap<>();
        for (int x : arr) p.merge(x, 1, Integer::sum);
        for (Map.Entry<Integer, Integer> e : p.entrySet())
            System.out.println(e.getKey() + " -> " + e.getValue());

        int maxFreq = 0, minFreq = arr.length, maxEl = 0, minEl = 0;
        for (Map.Entry<Integer, Integer> e : p.entrySet()) {
            if (e.getValue() > maxFreq) { maxFreq = e.getValue(); maxEl = e.getKey(); }
            if (e.getValue() < minFreq) { minFreq = e.getValue(); minEl = e.getKey(); }
        }
        System.out.println("\nHighest frequency element: " + maxEl + " Frequency: " + maxFreq);
        System.out.println("Lowest frequency element: " + minEl + " Frequency: " + minFreq);
    }
}
