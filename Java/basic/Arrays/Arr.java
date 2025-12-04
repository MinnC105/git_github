package Java.basic.Arrays;
import java.util.Scanner;
public class Arr {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] a = new int[10];
        // int[] a = {1, 2, 3, 4, 5};
        for (int i = 0; i < 10; ++i) {
            a[i] = sc.nextInt();
        }
        for (int i = 0; i < 10; ++i) {
            System.out.print(a[i] + " ");
        }
        sc.close();
    }
}
