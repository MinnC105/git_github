class Student():
    def __init__ (self):
        self.name = ""
        self.id = ""
        self.dob = ""
    def input(self):
        self.name = input("Student name: ")
        self.id = input("Student id: ")
        self.dob = input("Student dob: ")
    def display(self):
        print(f"Student: {self.name} ID: {self.id} DoB: {self.dob}")

class Course():
    def __init__ (self):
        self.name = ""
        self.id = ""
    def input(self):
        self.name = input("Course name: ")
        self.id = input("Course id: ")
    def display(self):
        print(f"Course: {self.name} ID: {self.id}")

class Mark():
    def __init__ (self):
        self.sid = ""
        self.cid = ""
        self.mark = 0
    def input (self):
        self.sid = input("Student id: ")
        self.cid = input("Course id: ")
        self.mark = input("Mark: ")
class MarkManagement():
    def __init__ (self):
        self.students = []
        self.courses = []
        self.marks = []
    def inputStudents (self):
        n = int(input("Enter number students: "))
        for _ in range(n):
            s = Student()
            s.input()
            self.students.append(s)
    def inputCourses (self):
        n = int(input("Enter number courses: "))
        for _ in range(n):
            c = Course()
            c.input()
            self.courses.append(c)
    def inputMarks (self):
        cid = input("Enter course id to put marks: ")
        check = any(c.id == cid for c in self.courses)  # check course exist
        if not check:
            print("Course not found")
            return
        for s in self.students:
            print(f"Enter mark for: {s.name} ID: {s.id}")
            mark = Mark()
            mark.sid = s.id
            mark.cid = cid
            mark.mark = input(f"Mark for {s.name}: ")
            self.marks.append(mark)
    def displayStudents (self):
        for s in self.students:
            s.display()
    def displayCourses (self):
        for c in self.courses:
            c.display()
    def displayMarks (self):
        for m in self.marks:
            m.display()

mm = MarkManagement()
mm.inputStudents()
mm.inputCourses()
mm.inputMarks()
mm.displayStudents()
mm.displayCourses()
mm.displayMarks()