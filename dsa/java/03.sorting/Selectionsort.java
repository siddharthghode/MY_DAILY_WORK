import java.util.*;

public class Selectionsort {

    static void sort(ArrayList<Integer> list, int n) {

        for(int i = 0; i <= n; i++) {

            int min = i;

            for(int j = i + 1; j <= n; j++) {

                if(list.get(j) < list.get(min)) {
                    min = j;
                }
            }

            Collections.swap(list,i,min);
        }
    }


    public static void main(String[] args) {

        ArrayList<Integer> list=new ArrayList<>(Arrays.asList(45,12,89,3,67,23,9,100));

        int n = list.size() - 1;

        sort(list,n);

        for(int i=0; i<=n; i++) {
            System.out.print(" "+list.get(i));
        }
    }
}