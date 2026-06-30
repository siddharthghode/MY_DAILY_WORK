import java.lang.reflect.Array;
import java.util.HashMap;

public class A07_find_the_number_occure_once {
    public static void main(String[] args) {

        int[] array = {
                12, 7, 12, 0, -5, 99, 7, 7,
                100, 0, 12, 45, 45, 45,
                -5, 99, 1, 2, 3, 3, 2, 1,
                100, 100, -100, 50, 50, 50, 50
        };

        // find the single element amoung doubles
        // for (int i = 0; i < array.length; i++) {
        //     int num = array[i];
        //     int count = 0;
        //     for (int j = 0; j < array.length; j++) {
        //         if (array[j] == num)
        //             count++;
        //     }
        //     if (count == 1) {
        //         System.out.println(num);
        //         break;
        //     }
        // }

        // better by using hashing
        // int[] array = { 1, 2, 2, 4, 3, 1, 4 };
        // HashMap<Integer, Integer> maap = new HashMap<>();
        // for (int i = 0; i < array.length; i++) {
        // maap.put(array[i], maap.getOrDefault(array[i], 0) + 1);
        // }
        // int get_one = 0;
        // for (int i = 0; i < array.length; i++) {
        // if (maap.get(array[i]) == 1) {
        // get_one = array[i];
        // break;
        // }
        // }
        // System.out.println(get_one);

        // optimized approch
        int xor = 0;
        for (int i = 0; i < array.length; i++) {
        xor = xor ^ array[i];
        }
        System.out.println(xor);
    }
}
