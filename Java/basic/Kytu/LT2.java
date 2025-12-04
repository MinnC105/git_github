package Java.basic.Kytu;
import java.util.Scanner;
public class LT2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // String s = "Code";
        // System.out.print(s.length());           // 4
        // System.out.print(s.charAt(2));          // d
        // Replace chuỗi/ lý tự
        // System.out.println("Cod3l3arn".replace('3', 'e'));  // Codelearn
        // System.out.println("Blackcat".replace("Black", "White"));   // Whitecat

        // String s = "CoDeLeArN";
		// System.out.println(s.toUpperCase());    // CODELEARN
		// System.out.println(s.toLowerCase());    // codelearn

        // IndexOf: trả vị trí xuất hiện đầu tiên của 1 String trong String khác, không có in -1
		// String s = "Codelearn";
		// System.out.println(s.indexOf("learn"));	// 4
		// System.out.println(s.indexOf("black"));	// -1

		// StartsWith, endsWith
		// String name = "Codelearn";
		// System.out.println(name.startsWith("Code"));	// true
		// System.out.println(name.startsWith("abc"));		// false
		// System.out.println(name.endsWith("rn"));		// true
		// System.out.println(name.endsWith("z"));			// false

		// Split: tách 1 xâu thành mảng các xâu
		// String s = "Welcome to codelearn!";
		// String[] words = s.split(" ");
		// for(String w: words) {
		// 	System.out.println(w);
		// }
		// Welcome 
		// to
		// codelearn!

		// Substring: lấy ra 1 xâu con dựa trên chỉ số bắt đầu và chỉ số kết thúc 
		// String name = "Codelearn";
		// System.out.println(name.substring(0, 2));   // Co
		// System.out.println(name.substring(0, 4));   // Code
		// System.out.println(name.substring(4));	   // learn
        sc.close();
	}
}

/*
* input: 2 xâu ký tự s1, s2 
* output: hiện ra vị trí đầu tiên mà s2 xuất hiện trong s1 (không phân biệt hoa thường)
* EG:
* input: s1 = "Codelearn", s2 = "LEARN"    s1 = "blackcat", s2 = "lack"
* output: 4 
*/
// String s1 = sc.next();
// String s2 = sc.next();
// s1 = s1.toLowerCase();
// s2 = s2.toLowerCase();
// System.out.print(s1.indexOf(s2));

// delete số trong string
/*
String s = sc.next();
// Cách 1:
// s = s.replaceAll("\\d", ""); // \\d nghĩa là [0-9]

// Cách 2:
// for (char c = '0'; c <= '9'; ++c) {
// s = s.replace(c + "", "");
// // s = s.replace(c, ""); // bị lỗi
// }

// c + "": ép kiểu char thành String để thành s.replace(String target, String
// replacement)
// target, replacement đều phải là String

// biến c ở đây là char ('0', '1', …)
// s.replace(c, ""); -> s.replace(char oldChar, char newChar) (thay ký tự
// thành ký tự, không phải thay = chuỗi rỗng)

// char c = '5';
// String str = c + ""; // "5"

System.out.println(s);
// codel343ea4rn
// codelearn
*/

// EG: in ra các ký tự
// for (char c = '0'; c <= '9'; c++) {
// System.out.print(c);
// }
// System.out.println();
// for(char c = 'a'; c <= 'z'; c++) {
// System.out.print(c);
// }

// EG: in ra số ký tự viết hoa trong string
// 		String s = sc.next();
// 		int answer = 0;
// 		for (int i = 0; i < s.length(); i++) {
// 			if (s.charAt(i) >= 'A' && s.charAt(i) <= 'Z') {
// 				answer++;
// 			}
// 		}
// 		System.out.print(answer);

// EG: reverse string
// 		String s = sc.next();
// 		String answer = "";
// 		for (int i = s.length() - 1; i >= 0; i--) {
// 			answer += s.charAt(i);
// 		}
// 		System.out.print(answer);


