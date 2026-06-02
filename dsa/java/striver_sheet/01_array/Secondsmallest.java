public class Secondsmallest {
    public static void main(String[] args) {
        int[] a={10,9,0,1,4,100};
        int smallest=a[0];
        int secondsmallest=-1;
        for(int i=1;i<a.length;i++)
        {
            if(smallest>a[i])
             {   secondsmallest=smallest;
                smallest=a[i];
             }
            else if(smallest<a[i] && a[i]<secondsmallest)
            {
                secondsmallest=a[i];
            }
        }
        System.out.println(secondsmallest);
    }
    
}
