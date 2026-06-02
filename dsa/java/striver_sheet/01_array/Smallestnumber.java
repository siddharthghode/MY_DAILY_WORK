public class Smallestnumber{
public static void main(String[] args)
{
    int[] arr={10,20,100,10000,-1};
        int smallest =arr[0];
        for(int i=arr.length-1;i>0;i--)
        {
            if(arr[i]<smallest) smallest = arr[i];
        }
        System.out.println(smallest);
}
}