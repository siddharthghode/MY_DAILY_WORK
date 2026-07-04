import java.util.ArrayList;

public class A34 {
    public static void main(String[] args) {
         long long n = 600851475143;
        long store = 0;
        ArrayList<Integer> primes = new ArrayList<>();
        for (long num = 2; num <= n; num++) {
            boolean isPrime = true;

            for (long i = 2; i * i <= num; i++) {
                if (num % i == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                primes.add(num);
            }
        }
        for (long i = 0; i < primes.size(); i++) {
            if (n % primes.get(i) == 0) {
                store = primes.get(i);
            }

        }
        System.out.println(store);
        // primes contains all prime numbers up to n
    }
}