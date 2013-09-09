/*Kiem thu giai phuong trinh bac nhat*/

public class test
{
	public static int giaiPT(int a, int b)
	{
		try{
			return -b/a;
		}catch(Exception e){
			return 0;
		}
	}

	public static void test1()
	{
		int ketquaThat = giaiPT(1,1);
		if (ketquaThat == -1)
		{
			System.out.println("test1 was success");
		}else{
			System.out.println("fail");
		}
	}

	public static void test2()
	{
		int ketquaThat = giaiPT(10,-90);
		if (ketquaThat == 9)
		{
			System.out.println("test2 was success");
		}else{
			System.out.println("fail");
		}
	}

	public static void test3()
	{
		int ketquaThat = giaiPT(0,-90);
		if (ketquaThat == 0)
		{
			System.out.println("test3 was success");
		}else{
			System.out.println("fail");
		}
	}

	public static void main(String args[])
	{
		int i = giaiPT(0,1);
		//System.out.println("Hello World");
		System.out.println("Test1:");
		test1();
		System.out.println("Test2:");
		test2();
		System.out.println("Test3:");
		test3();
	}
}