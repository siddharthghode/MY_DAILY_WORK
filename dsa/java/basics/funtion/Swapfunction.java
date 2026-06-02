public class Swapfunction {
    static void swaap(int a,int b)
    {
        int temp=a;
        a=b;
        b=temp;

    }
    public static void main(String[] args)
    {

        int a=9;
        int b=1;
        swaap(a,b);
        System.out.println(a+" "+b);
    }
}
