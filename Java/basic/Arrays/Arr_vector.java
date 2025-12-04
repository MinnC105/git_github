package Java.basic.Arrays;
// LT: ArrayList vs Array
// ArrayList<Integer> v = new ArrayList<>();
// import java.util.ArrayList;
// // Thêm phần tử
// v.add(10);
// v.add(20);
// // Lấy phần tử
// int x = v.get(0)
// // Sửa phần tử/ gán phần tử
// v.set(1, 99);
// // Kích thước
// int n = v.size();
// // Xóa phần tử
// v.remove(0);
// // Xóa hết
// v.clear();
// Note
// C++: vector <int> v(10, 5) khởi tạo 10 phần tử = 5
// Java không có syntax trên nên phải lặp để add
// for (int i = 0; i < 10; ++i) v.add(5);

import java.util.ArrayList;
// import java.util.Vector;
public class Arr_vector {
    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<>();
        // Vector<Integer> v = new Vector<>();  // old

        arr.add(10);
        arr.add(30);
        arr.add(11);

        System.out.println("Size = " + arr.size());
        System.out.println("Element[1] = " + arr.get(1));
        for (int x: arr) {
            System.out.print(x + " ");
        }
    }
}
