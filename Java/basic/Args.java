// Command-line arguments
package Java.basic;
public class Args {
    public static void main(String[] args) {
        // EG1:
        // System.out.println("Length: " + args.length);
        // for (String s : args) {
        //     System.out.println(s);
        // }
        // EG2:
        if (args.length < 2) {
            System.out.println("Need 2 numbers");
            return;
        }
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        System.out.println(a + b);
    }
}
// java Java.basic.Args hello minhchau 123 abc

/*
 * String[] args better than String args[] (old style in c/c++)
 * bắt buộc là String[] - mọi kiểu dữ liệu đầu vào java được coi là string
 * muốn dùng đúng kiểu dữ liệu -> dùng parse
 */