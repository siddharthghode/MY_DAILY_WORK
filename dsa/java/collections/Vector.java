import java.util.*;

public class Vector {
    public static void main(String[] args) {
        ArrayList<Integer> v = new ArrayList<>(Arrays.asList(1, 4, 5, 6, 8, 2));
        v.add(0);
        v.add(11);
        System.out.println(v.get(1));

        Collections.sort(v);
        System.out.println("after sorting");
        System.out.println(v);

        ArrayList<int[]> v1 = new ArrayList<>(Arrays.asList(
            new int[]{1,2}, new int[]{1,1}, new int[]{1,9}, new int[]{1,4}
        ));
        v1.add(new int[]{1,6}); v1.add(new int[]{2,1}); v1.add(new int[]{3,0}); v1.add(new int[]{1,7});

        v1.sort((a, b) -> a[0] != b[0] ? b[0] - a[0] : b[1] - a[1]);
        System.out.println("Sorted vector of pairs (desc):");
        for (int[] p : v1) System.out.print(p[0] + " " + p[1] + "||");
        System.out.println("\nSize: " + v1.size());
    }
}
