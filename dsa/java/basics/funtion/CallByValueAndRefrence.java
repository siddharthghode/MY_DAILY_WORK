public class CallByValueAndRefrence {
    static int changeValue(int a) {
        a = 10;
        System.out.println("inside function a: " + a);
        return a;
    }

    public static void main(String[] args) {
        int a = 5;
        System.out.println("the number before: " + a);
        changeValue(a);
        System.out.println("after function call: " + a);
    }
}
