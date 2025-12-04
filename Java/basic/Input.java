package Java.basic;
import java.util.Scanner;

public class Input {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // EG1:
        // char c = sc.next().charAt(0);
        // // char c = (char) (sc.next().charAt(0) + 2);
        // System.out.println(c);

        // EG2:
        int phone = sc.nextInt();
        // nextInt, Double, ... (exc: nextLine, next) tạo /n 
        sc.nextLine();  // loại bỏ /n
        String name = sc.nextLine();
        String address = sc.next();
        System.out.println("name: " + name);
        System.out.println("address: " + address);
        System.out.println("phone: " + phone);
        sc.close();
    }
}

// javac Java/basic/Input.java
// java Java.basic.Input