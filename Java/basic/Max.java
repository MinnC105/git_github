package Java.basic;
import java.util.Scanner;
public class Max {
    public static int max3(int a, int b, int c) {
        if(a >= b && a >= c) return a;
		if(b >= c) return b;
		return c;
    }
    public static void main(String[] arsg) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        
        if (a >= b && a >= c) {
            System.out.println(a);
        } else if (b >= c) {
            System.out.println(b);
        } else {
            System.out.println(c);
        }
        
        // System.out.println(max3(3, 1, 9));
        sc.close();
    }
}
