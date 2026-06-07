import java.util.LinkedList;

public class Queue {
    public static void main(String[] args) {
        java.util.Queue<Integer> q = new LinkedList<>();
        q.add(2); q.add(3); q.add(4); q.add(0);
        java.util.Queue<Integer> a = new LinkedList<>(q);
        while (!a.isEmpty()) { System.out.print("|" + a.peek()); a.poll(); }
        System.out.println();
        System.out.println(((LinkedList<Integer>) q).getLast());
    }
}
