public class SecondLargestNumber {
    public static void main(String[] args) {
        int[] arr = {10, 3, 99, 100, 2, 85};
        int largest=arr[0];
        int secondLargest=-1;
        for(int i=1;i<arr.length;i++)
        {
            if(arr[i]>largest)
            {
                secondLargest=largest;
                largest=arr[i];
            }
            else if (arr[i]<largest && arr[i]>secondLargest) {
                secondLargest=arr[i];
            }
        }
        System.out.println(secondLargest);
    }
}
