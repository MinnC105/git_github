import curses
import math
import numpy as np


class Student:
    def __init__(self, sid, name, dob):
        self.__sid = sid
        self.__name = name
        self.__dob = dob

    def get_sid(self):
        return self.__sid
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob


class Course:
    def __init__(self, cid, name, credit):
        self.__cid = cid
        self.__name = name
        self.__credit = credit

    def get_cid(self):
        return self.__cid
    def get_name(self):
        return self.__name
    def get_credit(self):
        return self.__credit


class Mark:
    def __init__(self, sid, cid, mark):
        self.__sid = sid
        self.__cid = cid
        self.__mark = mark

    def get_sid(self):
        return self.__sid
    def get_cid(self):
        return self.__cid
    def get_mark(self):
        return self.__mark



def cal_gpa (student, courses, marks):
    scores = []
    credits = []
    for c in courses:
        check = False
        for m in marks:
            if m.get_sid() == student.get_sid() and m.get_cid() == c.get_cid():
                scores.append(m.get_mark())
                credits.append(c.get_credit())
                check = True
                break
        if not check:
            scores.append(0.0)
            credits.append(c.get_credit())

    scores = np.array(scores)
    credits = np.array(credits)

    if credits.sum() == 0:
        return 0.0
    return np.sum(scores * credits) / np.sum(credits)


"""
    # stdscr.addstr() → hiển thị prompt
    # stdscr.getch()
    # stdscr.getstr()
    # stdscr.clear()
    # getstr → nhập chuỗi
    # echo/noecho → bật/tắt hiện ký tự
"""
class CursesUI:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.current = 0    # vị trí menu đang chọn

        self.students = []
        self.courses = []
        self.marks = []

        self.menu = [
            "Add students",
            "Add courses",
            "Add marks",
            "Show students + GPA",
            "Show courses",
            "Exit"
        ]

    def input_str(self, y, x, prompt):
        curses.echo()
        self.stdscr.addstr(y, x, prompt)   
        self.stdscr.refresh()
        # refresh() : addstr() ghi promt vào buffer, refresh() đẩy buffer ra màn 
        s = self.stdscr.getstr(y, x + len(prompt), 30).decode()
        # 30 : max ký tự được nhập 
        # decode() : getstr() trong curses trả về bytes , decode() để chuyển về 
        curses.noecho()
        return s

    def input_int(self, y, x, prompt):
        while True:
            try:
                return int(self.input_str(y, x, prompt))
            except ValueError:
                self.stdscr.addstr(y + 1, x, "Invalid number!")

    def input_float(self, y, x, prompt):
        while True:
            try:
                return float(self.input_str(y, x, prompt))
            except ValueError:
                self.stdscr.addstr(y + 1, x, "Invalid number!")

    # INPUT IMPLEMENT 
    def input_students(self):
        self.stdscr.clear()    
        # clear() : xóa màn hình hiển thị trước 
        n = self.input_int(2, 2, "Number of students: ")
        for i in range(n):
            self.stdscr.clear()
            self.stdscr.addstr(1, 2, f"Student {i+1}")
            sid = self.input_str(3, 2, "ID: ")
            name = self.input_str(4, 2, "Name: ")
            dob = self.input_str(5, 2, "DOB: ")
            self.students.append(Student(sid, name, dob))
        self.stdscr.getch()
        # getch() : = “Press any key to continue”

    def input_courses(self):
        self.stdscr.clear()
        n = self.input_int(2, 2, "Number of courses: ")
        for i in range(n):
            self.stdscr.clear()
            self.stdscr.addstr(1, 2, f"Course {i+1}")
            cid = self.input_str(3, 2, "Course ID: ")
            name = self.input_str(4, 2, "Name: ")
            credit = self.input_int(5, 2, "Credit: ")
            self.courses.append(Course(cid, name, credit))
        self.stdscr.getch()

    def input_marks(self):
        self.stdscr.clear()
        cid = self.input_str(2, 2, "Course ID: ")
        check = False 
        for c in self.courses:
            if c.get_cid() == cid:
                for s in self.students:
                    mark = self.input_float(4, 2, f"Mark for {s.get_sid()}: ")
                    mark = math.floor(mark * 10) / 10
                    self.marks.append(Mark(s.get_sid(), cid, mark))
                check = True 
                break 
        if not check:
            self.stdscr.addstr(6, 2, "Course not exist!")
        # print ra "Course not exist !
        self.stdscr.getch()

    def show_students(self):
        self.stdscr.clear()
        
        data = [] 
        for s in self.students:
            gpa = cal_gpa(s, self.courses, self.marks)
            data.append((s, gpa)) 
        data.sort(key = lambda x: x[1], reverse = True)

        y = 2 
        for s, gpa in data:
            self.stdscr.addstr(y, 2, f"{s.get_sid()} | {s.get_name()} | GPA: {gpa:.2f}")
            y += 1
        self.stdscr.getch()

    def show_courses(self):
        self.stdscr.clear()
        y = 2
        for c in self.courses:
            self.stdscr.addstr(y, 2, f"{c.get_cid()} | {c.get_name()} | {c.get_credit()}")
            y += 1
        self.stdscr.getch()

    #   MENU 
    def draw_menu(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 2, "STUDENT MANAGEMENT (CURSES)", curses.A_BOLD)
        for i, item in enumerate(self.menu):
            if i == self.current:
                self.stdscr.addstr(i + 2, 4, item, curses.A_REVERSE)
                # curses.A_REVERSE    # chữ trắng, nền đen và ngược 
                # curses.A_BOLD       # in đậm
                # curses.A_UNDERLINE  # gạch chân
                # curses.color_pair() # màu tùy chỉnh
            else:
                self.stdscr.addstr(i + 2, 4, item)
        self.stdscr.refresh()

    def run(self):
        curses.curs_set(0)          # tắt/ bật hiện chuột 
        self.stdscr.keypad(True)    
        # hàm sẵn cho phép sử dụng mũi tên bàn phím , getch() không in ra giá trị rác

        while True:
            self.draw_menu()
            key = self.stdscr.getch()

            if key == curses.KEY_UP and self.current > 0:
                self.current -= 1
            elif key == curses.KEY_DOWN and self.current < len(self.menu) - 1:
                self.current += 1
            elif key in (10, 13):
                if self.current == 0:
                    self.input_students()
                elif self.current == 1:
                    self.input_courses()
                elif self.current == 2:
                    self.input_marks()
                elif self.current == 3:
                    self.show_students()
                elif self.current == 4:
                    self.show_courses()
                elif self.current == 5:
                    break


def main(stdscr):
    ui = CursesUI(stdscr)
    ui.run()

curses.wrapper(main)
# wrapper 


"""
CLI                 UI curses
print               stdscr.addstr
input               stdscr.getch
while True          vòng lặp UI
menu số             menu highlight
"""
        
# curse không dùng print, input:
# stdscr.addstr()
# stdscr.getch()
# stdscr.getstr()