public class PrintAllDivisors {
    public static void main(String[] args) {
        int n = 4;
        int i=1;
        while(i<=n)
	{
		if(n%i==0) 
		{
			System.out.println(i);
		}
		i++;
	}	
    }
}
