package Java.basic.Arrays;
import java.util.Scanner;
public class Arr_2d {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] a = new int[n][m];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                a[i][j] = sc.nextInt();
            }
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                System.out.println("a[" + i + "][" + j + "] = " + a[i][j]);
            }
        }
        sc.close();
    }
}
/* n = 2, m = 3, arr = [[5, 7, 3], [1, 2, 4]]
2 3
5 7 3
1 2 4
*/
