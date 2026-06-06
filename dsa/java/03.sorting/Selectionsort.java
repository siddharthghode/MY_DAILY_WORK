import java.util.*;

public class Selectionsort {

    static void sort(int[] array, int n) {

        for(int i = 0; i <= n; i++) {

            int min = i;

            for(int j = i + 1; j <= n; j++) {

                if(array[j] < array[min]) {
                    min = j;
                }
            }

            int temp = array[i];
            array[i] = array[min];
            array[min] = temp;
        }
    }


    public static void main(String[] args) {

        int[] array = {45,12,89,3,67,23,9,100};

        int n = array.length - 1;

        sort(array,n);

        for(int i=0; i<=n; i++) {
            System.out.println(array[i]);
        }
    }
}