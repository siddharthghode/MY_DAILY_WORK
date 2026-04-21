public class Demo {

    static int getInt() {
        return 10;
    }

    static String getString() {
        return "Hello";
    }

    static void show() {
        System.out.println("No return");
    }

    public static void main(String[] args) {
        int a = getInt();
        String s = getString();
        show();

        System.out.println(a);
        System.out.println(s);
    }
}