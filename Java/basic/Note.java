package Java.basic;
public class Note {
    public static void main(String[] args) {
        int c = 0;
        for (int i = 0; i < 5; ++i) {
            for (int j = 0; j < 5; ++j) {
                System.out.print(c + " ");
                c += 1;
                System.out.print(5 * i + j + " ");
            }
            System.out.println();
        }
    }
}