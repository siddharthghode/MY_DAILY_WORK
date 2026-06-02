public class Sorted
{
    public static void main(String[] args)
    {
        int[] arr={1,2,1,4,5,6};
        int i=1;
        while (i<arr.length) {
            if(arr[i]>=arr[i-1])
            {
                i++;
            }
            else{
                break;
            }
        }
        System.out.println(i);
        if(i==arr.length) System.out.println("Sorted");
        else System.out.println("not sorted");
    }
}