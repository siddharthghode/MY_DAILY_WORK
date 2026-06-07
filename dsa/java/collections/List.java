import java.util.Collections;
import java.util.LinkedList;

public class List {
    public static void main(String[] args) {
        LinkedList<Integer> ls = new LinkedList<>();
        ls.add(2); ls.add(4); ls.add(6); ls.add(0); ls.add(1);
        System.out.print("\nprint list items");
        for (int x : ls) System.out.print(x + "||");
        Collections.sort(ls);
        System.out.print("\nsort::");
        for (int x : ls) System.out.print(x + "||");
        System.out.print("\nsize of list:");
        System.out.println(ls.size());
    }
}
