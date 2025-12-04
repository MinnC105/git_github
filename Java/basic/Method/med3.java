package Java.basic.Method;

import java.util.Scanner;

public class med3 {
    // EG: tính tổng
    public static int sum(int[] arr, int n) {
        if (n == 1)
            return arr[0];
        return arr[n - 1] + sum(arr, n - 1);
    }
    // EG: tính tổng số lẻ 1 đến n
    public static int sumo(int n) {
        if (n == 1)
            return 1;
        if (n % 2 == 0)
            return sumo(n - 1);
        return n + sumo(n - 1);
    }
    // EG: factorial
    public static int fac(int n) {
        if (n == 1 || n == 0) return 1;
        return n * fac(n - 1);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; ++i) {
            arr[i] = sc.nextInt();
        }
        System.out.println(sum(arr, n));
        System.out.println(sumo(5));
        System.out.println(fac(4));
        sc.close();
    }
}
