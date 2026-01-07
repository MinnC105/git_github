import curses
import math
import numpy as np

from domains import Student, Course, Mark


class InputSystem:
    def __init__(self, stdscr, students, courses, marks):
        self.stdscr = stdscr
        self.students = students
        self.courses = courses
        self.marks = marks 


    def save_students(self):
        with open("students.txt", "w", encoding="utf-8") as f:
            for s in self.students:
                f.write(f"{s.get_sid()} | {s.get_name()} | {s.get_dob()}\n")
    
    def save_courses(self):
        with open("courses.txt", "w", encoding="utf-8") as f:
            for c in self.courses:
                f.write(f"{c.get_cid()} | {c.get_name()} | {c.get_credit()}\n")

    def save_marks(self):
        with open("marks.txt", "w", encoding="utf-8") as f:
            for m in self.marks:
                f.write(f"{m.get_sid()} | {m.get_cid()} | {m.get_mark()}\n")


    def input_str(self, y, x, prompt):
        curses.echo()
        self.stdscr.addstr(y, x, prompt)   
        self.stdscr.refresh()
        s = self.stdscr.getstr(y, x + len(prompt), 30).decode()
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

    def input_students(self):
        self.stdscr.clear()    
        n = self.input_int(2, 2, "Number of students: ")
        for i in range(n):
            self.stdscr.clear()
            self.stdscr.addstr(1, 2, f"Student {i+1}")
            sid = self.input_str(3, 2, "ID: ")
            name = self.input_str(4, 2, "Name: ")
            dob = self.input_str(5, 2, "DOB: ")
            self.students.append(Student(sid, name, dob))
        
        self.save_students()
        self.stdscr.getch()

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
        
        self.save_courses()
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
                
                self.save_marks()
                break 
        if not check:
            self.stdscr.addstr(6, 2, "Course not exist!")
        self.stdscr.getch()
