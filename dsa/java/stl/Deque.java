import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;

public class Deque {
    public static void main(String[] args) {
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        dq.addLast(3); dq.addFirst(8); dq.addLast(1); dq.addFirst(19);
        for (int x : dq) System.out.print(x + "||");
        System.out.println();
        ArrayList<Integer> sorted = new ArrayList<>(dq);
        Collections.sort(sorted);
        for (int x : sorted) System.out.print(x + "||");
        System.out.println(dq.size());
    }
}
