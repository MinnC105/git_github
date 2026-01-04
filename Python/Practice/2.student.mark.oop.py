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
    def __init__ (self, cid, name):
        self.__cid = cid
        self.__name = name

    def set_cid (self, cid):
        self.__cid = cid
    def set_name (self, name):
        self.__name = name

    def get_cid (self):
        return self.__cid
    def get_name (self):
        return self.__name


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
    def input(self):
        pass
    def list(self):
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
            self.courses.append(Course(cid, cname))

    def inp_m (self):
        res = input("Course ID want to choose: ")
        for c in self.courses:
            if res == c.get_cid():
                for s in self.students:    
                    sid = s.get_sid()
                    mark = float(input(f"Enter mark for {s.get_sid()}: "))
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

    def list_s (self):
        print("STUDENT LIST")
        for s in self.students:
            print(f"{s.get_sid()}|{s.get_name()}|{s.get_dob()}")
        
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
                        
class ManagementSystem:
    def __init__ (self):
        students = []
        courses = []
        marks = []

        i = InputSystem(students, courses, marks)
        o = OutputSystem(students, courses, marks)
        i.input()
        o.list()

m = ManagementSystem()