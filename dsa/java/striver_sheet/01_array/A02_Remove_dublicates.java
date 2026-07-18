import java.util.*;

public class A02_Remove_dublicates {

    static void remove_dub(ArrayList<Integer> list) {
        int i = 0;
        for (int j = 1; j < list.size(); j++) {

            if (!list.get(i).equals(list.get(j))) {
                i++;
                list.set(i, list.get(j));
            }
        }

        int k = i + 1;

        while (k < list.size()) {
            list.remove(k);
        }
    }

    public static void main(String[] args) {

        ArrayList<Integer> list = new ArrayList<>(Arrays.asList(5, 2, 1, 3, 2, 5, 4, 1, 3));
        // Collections.sort(list);
        // remove_dub(list);
        HashSet<Integer> seet = new HashSet<>();
        for (int x : list) {
            seet.add(x);
        }
        System.out.println(seet);

        // System.out.println("After removing duplicates:");
        // System.out.println(list);
    }
}