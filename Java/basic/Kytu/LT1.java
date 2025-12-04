package Java.basic.Kytu;
import java.util.Scanner;
public class LT1 {
    public static void main(String[] args) {
        // in ra các ký tự trong string
        String s = "CodeLearn";
        System.out.println(s.length());
        for (int i = 0; i < s.length(); ++i) {
            System.out.println(s.charAt(i));
        }
        for (char c: s.toCharArray()) {
            System.out.println(c);
        }
        // in ra ký tự thứ k
        Scanner sc = new Scanner(System.in);
        String t = sc.next();
        int k = sc.nextInt();
        System.out.print(t.charAt(k - 1));
        // in ra số lần xuất hiện của ký tự c
        String st = sc.next();
		char ch = sc.next().charAt(0);
		int ans = 0;
		for (int i = 0; i < st.length(); i++) {
			if(st.charAt(i) == ch) {
				ans ++;
			}
		}
		System.out.print(ans);
        sc.close();
    }
}
