public class Insertionsort{
    static void sort(int[] array,int n)
    {
      for(int i=1;i<n;i++)
      {
        int j=i;
        while(j>0 && array[j-1]>array[j])
        {
          int temp=array[j-1];
          array[j-1]=array[j];
          array[j]=temp;

          j--;
        }
      }
    }
    public static void main(String[] args)
    {
     int[] array={45,12,89,3,67,23,9,100};
     int n=array.length;
     sort(array,n);
     for(int x:array)
     {
      System.out.println(x);
     }
    }
}