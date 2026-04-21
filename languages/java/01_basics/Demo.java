public class Demo {

    static int add(int a, int b) {   // static + return + parameters
        return a + b;
    }

    void greet() {                   // non-static + no return
        System.out.println("Hello");
    }

    public static void main(String[] args) {
        int result = add(2, 3);
        System.out.println(result);

        Demo d = new Demo();
        d.greet();
    }
}