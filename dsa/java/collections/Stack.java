import java.util.Stack;

public class Stack {
    public static void main(String[] args) {
        java.util.Stack<Integer> st = new java.util.Stack<>();
        st.push(1); st.push(4); st.push(7);
        st.pop();
        java.util.Stack<Integer> v = new java.util.Stack<>();
        v.addAll(st);
        while (!v.isEmpty()) { System.out.print("||" + v.peek()); v.pop(); }
    }
}
