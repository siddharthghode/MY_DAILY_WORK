import java.util.HashMap;

public class A07_find_the_number_occure_once {
    public static void main(String[] args) {
        // find the single element amoung doubles
        // int[] array = { 1, 2, 2, 4, 3, 1, 4 };
        // for (int i = 0; i < array.length; i++) {
        // int num = array[i];
        // int count = 0;
        // for (int j = 0; j < array.length; j++) {
        // if (array[j] == num)
        // count++;
        // }
        // if (count == 1) {
        // System.out.println(num);
        // break;
        // }

        // }

        // by using hashing
        int[] array = { 1, 2, 2, 4, 3, 1, 4 };
        HashMap<Integer, Integer> maap = new HashMap<>();
        for (int i = 0; i < array.length; i++) {
            maap.put(array[i], maap.getOrDefault(array[i], 0) + 1);
        }
        int get_one = 0;
        for (int i = 0; i < array.length; i++) {
            if (maap.get(array[i]) == 1) {
                get_one = array[i];
                break;
            }
        }
        System.out.println(get_one);
    }
}
