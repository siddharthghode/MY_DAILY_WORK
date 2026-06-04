public class BinaryToDecimal{
    public static void main(String[] args)
    {
        int binary=11101;
        int decimal=0;
        int lnum;
        int count=0;
        while(binary>0)
        {   
            lnum=binary%10;
            decimal+=(Math.pow(2,count))*lnum;
            count++;
            binary=binary/10;
        }
        System.out.println(decimal);
    }
}