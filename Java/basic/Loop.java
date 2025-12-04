package Java.basic;
import java.util.Scanner;
public class Loop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // EG1:
        // int n = sc.nextInt();
        // for (int i = 0; i <= n; i += 2) {
        //     System.out.print(i + " ");
        // }
        // System.out.println();
        // int j = 0;
        // while (j <= n) {
        //     System.out.print(j + " ");
        //     j += 2;
        // }
        // System.out.println();
        // for (int i = n; i >= -n; --i) {
        //     System.out.print(i + " ");
        // }
        for (int i = 10; i > 1; --i) {
            System.out.print(i + " ");
        }

        // EG2: 
        // luôn chạy ít nhất 1 lần, chạy trước check
        int k = 1;
        do {
            System.out.print("do-while");
        } while (k < 1);
        // check trước chạy
        while (k < 1) {
            System.out.printf("while");
        }
        
        // EG3:
        for (int i = 1; i <= 100; i++) {
			if (i % 2 == 0) {
				continue;
			}
			System.out.print(i + " ");
		}
        sc.close();
    }
}
