import java.util.ArrayList;

public class A05_union_of_two_sorted_array_optimized {
    public static void main(String[] args)
    {
       int[] arr1 = {1, 2, 3, 4, 5};
       int n1=arr1.length;
       int[] arr2 = {2, 3, 5, 6, 7};
       int n2=arr2.length;
       ArrayList<Integer> list=new ArrayList<>();
       int i=0;
       int j=0;
       while (i<n1 && j<n2) {
         if(arr1[i]<=arr2[j])
            if(list.size()==0 || list.get(list.get(list.size()-1))!=arr1[i])
            {
                list.add(arr1[i]);
                i++;
            }
          else{
            if(list.size()==0 || list.get(list.get(list.size()-1))!=arr2[j])
            {
                list.add(arr2[j]);
                j++;
}
} 
    }
    while (j<n2) {
        if(list.size()==0 || list.get(list.get(list.size()-1))!=arr2[j])
            {
                list.add(arr1[i]);
                j++;
          }
    }
    while(i<n1)
    {
        if(list.size()==0 || list.get(list.get(list.size()-1))!=arr1[i])
            {
                list.add(arr1[i]);
                i++;
            }
    }
    System.out.println(list);
}
}
