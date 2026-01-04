package Java.Package.Package1;
import Java.Package.Package2.HelloMessage;
public class HelloNote {
    public static void main(String[] args) {
        HelloMessage m = new HelloMessage();
        m.sayHello();
    }
}

// package Java.Package.Package1;
// public class HelloNote {
//     public static void main(String[] args) {
//         Java.Package.Package2.HelloMessage m = new Java.Package.Package2.HelloMessage();
//         m.sayHello();
//     }
// }

// javac Java/Package/Package1/HelloNote.java
// java Java.Package.Package1.HelloNote
