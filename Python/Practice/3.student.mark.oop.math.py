import math
import numpy as np

class Student:
    def __init__ (self, sid, name, dob):
        self.__sid = sid
        self.__name = name
        self.__dob = dob

    def set_sid (self, sid):
        self.__sid = sid
    def set_name (self, name):
        self.__name = name
    def set_dob (self, dob):
        self.__dob = dob

    def get_sid (self):
        return self.__sid
    def get_name (self):
        return self.__name
    def get_dob (self):
        return self.__dob
    

class Course:
    def __init__ (self, cid, name, credit):
        self.__cid = cid
        self.__name = name
        self.__credit = credit

    def set_cid (self, cid):
        self.__cid = cid
    def set_name (self, name):
        self.__name = name
    def set_credit (self, credit):
        self.__credit = credit

    def get_cid (self):
        return self.__cid
    def get_name (self):
        return self.__name
    def get_credit (self):
        return self.__credit


class Mark:
    def __init__ (self, cid, sid, mark = 0.0):
        self.__cid = cid
        self.__sid = sid
        self.__mark = mark

    def set_cid (self, cid):
        self.__cid = cid
    def set_sid (self, sid):
        self.__sid = sid
    def set_mark (self, mark):
        self.__mark = mark

    def get_cid (self):
        return self.__cid
    def get_sid (self):
        return self.__sid
    def get_mark (self):
        return self.__mark


class System:
    def input (self):
        pass
    def list (self):
        pass


class InputSystem(System):
    def __init__ (self, students, courses, marks):
        self.students = students
        self.courses = courses
        self.marks = marks

    def input (self):
        self.inp_s()
        self.inp_c()
        self.inp_m()

    def inp_s (self):
        n = int(input("Enter number of students: "))
        for i in range(n):
            print(f"Student {i + 1}")
            sid = input("Student ID: ")
            sname = input("Name: ")
            dob = input("Date of Birth: ")
            self.students.append(Student(sid, sname, dob))

    def inp_c (self):
        m = int(input("Enter number of course: "))
        for i in range(m):
            print(f"Course {i + 1}")
            cid = input("Course ID: ")
            cname = input("Course name: ")
            credit = int(input("Credit: "))
            self.courses.append(Course(cid, cname, credit))

    def inp_m (self):
        res = input("Course ID want to choose: ")
        for c in self.courses:
            if res == c.get_cid():
                for s in self.students:    
                    sid = s.get_sid()
                    tmp = float(input(f"Enter mark for {s.get_sid()}: "))
                    mark = math.floor(tmp * 10) / 10
                    self.marks.append(Mark(res, sid, mark))
                return
        print("Invalid course ID")


class OutputSystem(System):
    def __init__ (self, students, courses, marks):
        self.students = students
        self.courses = courses
        self.marks = marks

    def list (self):
        self.list_s()
        self.list_c()
        self.list_m()
        self.list_gpa_desc()

    def list_s (self):
        print("STUDENT LIST (with GPA)")
        for s in self.students:
            gpa = cal_gpa(s, self.courses, self.marks)
            print(f"{s.get_sid()}|{s.get_name()}|{s.get_dob()}|GPA: {round(gpa, 2)}")

    def list_c (self):
        print("COURSE LIST")
        for c in self.courses:
            print(f"{c.get_cid()}|{c.get_name()}")

    def list_m (self):
        res = input("Course ID want to choose: ")
        for m in self.marks:
            if m.get_cid() == res:
                for s in self.students:
                    if s.get_sid() == m.get_sid():
                        print(f"{s.get_name()}: {m.get_mark()}")

    def list_gpa_desc (self):
        print("STUDENT SORTED BY GPA")
        data = []
        for s in self.students:
            gpa = cal_gpa(s, self.courses, self.marks)
            data.append((s, gpa))
        # data.sort(key = lambda x: x[1]) # defaut asc
        data.sort(key = lambda x: x[1], reverse = True)
        for s, gpa in data:
            print(f"{s.get_sid()}|{s.get_name()}|GPA: {round(gpa, 2)}")


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


class ManagementSystem:
    def __init__ (self):
        self.students = []
        self.courses = []
        self.marks = []

        i = InputSystem(self.students, self.courses, self.marks)
        o = OutputSystem(self.students, self.courses, self.marks)

        while True:
            print("1. Create list students")
            print("2. Create list courses")
            print("3. Add students")
            print("4. Add courses")
            print("5. Add marks")
            print("6. List students + GPA")
            print("7. List courses")
            print("8. List students + GPA (DESC)")
            print("0. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.students.clear()
                self.marks.clear()
                i.inp_s()

            elif choice == "2":
                self.courses.clear()
                self.marks.clear()
                i.inp_c()

            elif choice == "3":
                i.inp_s()

            elif choice == "4":
                i.inp_c()

            elif choice == "5":
                i.inp_m()

            elif choice == "6":
                o.list_s()

            elif choice == "7":
                o.list_c()

            elif choice == "8":
                o.list_gpa_desc()

            elif choice == "9":
                o.list_m()

            elif choice == "0":
                print("Exit program.")
                break

            else:
                print("Invalid choice!")

m = ManagementSystem()
