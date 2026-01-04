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


class InputSystem:
    def __init__ (self):
        self.__courses = []
        self.__students = []
        self.__marks = []
    
    def get_courses (self):
        return self.__courses
    def get_students (self):
        return self.__students
    def get_marks (self):
        return self.__marks
    
    def inp_s (self):
        n = int(input("Enter number of students: "))
        for i in range(n):
            print(f"Student {i + 1}")
            sid = input("Student ID: ")
            sname = input("Name: ")
            dob = input("Date of Birth: ")
            self.__students.append(Student(sid, sname, dob))

    def inp_c (self):
        m = int(input("Enter number of course: "))
        for i in range(m):
            print(f"Course {i + 1}")
            cid = input("Course ID: ")
            cname = input("Course name: ")
            self.__courses.append(Course(cid, cname))

    def inp_m (self):
        res = input("Course ID want to choose: ")
        for c in self.__courses:
            if res == c.get_cid():
                for s in self.__students:    
                    sid = s.get_sid()
                    mark = float(input(f"Enter mark for {s.get_sid()}: "))
                    self.__marks.append(Mark(res, sid, mark))
                return
        print("Invalid course ID")


class OutputSystem:
    def __init__ (self, students, courses, marks):
        self.__courses = courses
        self.__students = students
        self.__marks = marks
    
    def list_s(self):
        print("STUDENT LIST")
        for s in self.__students:
            print(f"{s.get_sid()}|{s.get_name()}|{s.get_dob()}")
        
    def list_c(self):
        print("COURSE LIST")
        for c in self.__courses:
            print(f"{c.get_cid()}|{c.get_name()}")
            
    def list_m(self):
        res = input("Course ID want to choose: ")
        for m in self.__marks:
            if m.get_cid() == res:
                for s in self.__students:
                    if s.get_sid() == m.get_sid():
                        print(f"{s.get_name()}: {m.get_mark()}")


class ManagementSystem:
    def __init__ (self):
        inputSystem = InputSystem()
        inputSystem.inp_s()
        inputSystem.inp_c()
        inputSystem.inp_m()

        self.students = inputSystem.get_students()
        self.courses = inputSystem.get_courses()
        self.marks = inputSystem.get_marks()

        outputSystem = OutputSystem(self.students, self.courses, self.marks)

        outputSystem.list_s()
        outputSystem.list_c()
        outputSystem.list_m()
        
m = ManagementSystem()


