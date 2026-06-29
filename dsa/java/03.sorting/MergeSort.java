import java.util.*;

public class MergeSort {

    static ArrayList<Integer> merge(int[] arr, int low, int mid, int high) {
        int left = low;
        int right = mid + 1;
        ArrayList<Integer> list = new ArrayList<>();
        while (left <= mid && right <= high) {
            if (arr[left] <= arr[right]) {
                list.add(arr[left]);
                left++;
            } else {
                list.add(arr[right]);
                right++;
            }
        }
        while (left <= mid) {
            list.add(arr[left]);
            left++;
        }
        while (right <= high) {
            list.add(arr[right]);
            right++;
        }
        System.out.println("Merged (" + low + "," + high + ") : " + list);
        for (int i = low; i <= high; i++) {
            arr[i] = list.get(i - low);
        }
        System.out.println(list);
        return list;
    }

    static void mergesort(int[] arr, int low, int high) {
        if (low < high) {
            int mid = (low + high) / 2;
            mergesort(arr, low, mid);
            mergesort(arr, mid + 1, high);
            merge(arr, low, mid, high);
        }

    }

    public static void main(String[] args) {
        int[] arr = { 38, 27, 43, 3, 9, 82, 10 };
        mergesort(arr, 0, arr.length - 1);

        // for (int i : arr)
        // System.out.print(i + " ");

    }
}
