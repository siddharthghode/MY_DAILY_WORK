public class Armstrong{
  public static void main(String[] args)
  {
    int num=153;
    int sum=0;
    int count=0;
    int temp=num;
    int lnum;
    while(temp>0)
    {
        count++;
        temp=temp/10;
    }
    temp=num;
    while(temp>0)
    {
        lnum=temp%10;
        sum+=Math.pow(lnum,count);
        temp=temp/10;

    }
    System.out.println(sum==num ? "Armstrong" : "not Armstrong");
  }
}