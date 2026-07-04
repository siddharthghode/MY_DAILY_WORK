public class A13_buy_sell {

    public void profit(int[] arr, int n) {
        int profit = 0;
        int buy = arr[0];
        for (int i = 1; i < n; i++) {
            if (buy > arr[i])
                buy = arr[i];
            profit = Math.max(profit, arr[i] - buy);
        }
        System.out.println(profit);
    }

    public static void main(String args[]) {
        int[] arr = { 7, 1, 5, 3, 6, 4 };
        int n = arr.length;
        A13_buy_sell obj = new A13_buy_sell();
        obj.profit(arr, n);
    }
}