public class A33 {

    static int fibonacci(int n) {

        if (n <= 2)
            return n;

        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {

        int n = 1;
        int sum = 0;

        while (true) {

            int fib = fibonacci(n);

            if (fib > 4000000)
                break;

            if (fib % 2 == 0)
                sum += fib;

            n++;
        }

        System.out.println(sum);
    }
}