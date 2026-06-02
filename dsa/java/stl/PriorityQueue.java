import java.util.Collections;

public class PriorityQueue {
    public static void main(String[] args) {
        // max heap
        java.util.PriorityQueue<Integer> pq = new java.util.PriorityQueue<>(Collections.reverseOrder());
        pq.add(2); pq.add(4); pq.add(7);
        System.out.println(pq.peek()); pq.poll();
        System.out.println(pq.peek()); pq.poll();
        System.out.println(pq.peek()); pq.poll();

        // min heap
        java.util.PriorityQueue<Integer> pq1 = new java.util.PriorityQueue<>();
        pq1.add(10); pq1.add(2); pq1.add(6); pq1.add(9); pq1.add(11);
        while (!pq1.isEmpty()) { System.out.print("|" + pq1.peek()); pq1.poll(); }
    }
}
