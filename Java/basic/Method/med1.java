package Java.basic.Method;
import java.util.Scanner;
// có giá trị trả về cần khai báo datatype: in, String, double, ...
// void: no return any value, method done code block or print
// void(có tham số hoặc không)
public class med1 {
// EG: in nb % 3 == 0 but not % 5 == 0 (just hiển thị , không yêu cầu trả về kết quả nên dùng void)
    public static void show(int[] arr) {
        for (int i = 0; i < arr.length; ++i) {
            if (arr[i] % 3 == 0 && arr[i] % 5 != 0) {
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println();
    }
// EG: in 3 lần từ 1 đến 10
    // có tham số
    public static void meo(int n) {
        for (int i = 1; i <= n; ++i) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
    // không tham số
    public static void dog() {
        for (int i = 1; i <= 10; ++i) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
// EG: count even
    public static int quec(int[] arr) {
        int ans = 0;
        for (int i = 0; i < arr.length; ++i) {
            if (arr[i] % 2 == 0) {
                ans++;
            } 
        }
        return ans;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; ++i) {
            arr[i] = sc.nextInt();
        }
        show(arr);
        meo(5);
        dog();
        
        int[] arr1 = {1, 2, 3};
        int[] arr2 = {2, 2, 7, 3};
        int[] arr3 = {8, 2, 2, 5};
        System.out.println(quec(arr1));
        System.out.println(quec(arr2));
        System.out.println(quec(arr3));
        sc.close();
    }
}
