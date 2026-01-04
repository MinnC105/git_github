package Java.Package.Package1;
import Java.Package.Package2.Hello2; 

public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello from Hello in Package1!");

        Hello2.sayHi("Package2");
    }
}

