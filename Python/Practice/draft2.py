class Student():
    def __init__ (self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
    def get_id (self):
        return self.__id
    def get_name (self):
        return self.__name
    def get_dob (self):
        return self.__dob
    def set_id (self, id):
        self.__id = id
    def set_name (self, name):
        self.__name = name
    def set_dob (self, dob):
        self.__dob = dob
    def __str__ (self): 
        return f"Student ID: {self.__id}, Name: {self.__name}, DoB: {self.__dob}"

class Course():
    def __init__ (self, id, name):
        self.__id = id
        self.__name = name
    def get_id (self):
        return self.__id
    def get_name (self):
        return self.__name
    def set_id (self, id):
        self.__id = id
    def set_name (self, name):
        self.__name = name
    def  __str__ (self):
        return f"Course ID: {self.__id}, Name: {self.__name}"
    
class Management():
    def __init__ (self):
        self.__students = []
        self.__courses = []
    # input
    def inp_std (self):
        print("Add new student")
        sid = input("Student ID: ")
        name = input("Name: ")
        dob = input("Date of birth (DD/MM/YYYY): ")
        if not sid or not name:
            print("ID and Name can't empty")
            return None
        return Student(sid, name, dob)
    def inp_course (self):
        print("Add new course")
        cid = input("Course ID: ")
        name = input("Course name: ")
        if not cid or not name:
            print("ID and Name can't empty")
            return None
        return Course(cid, name)
    # display
    def dis_std (self):
        if not self.__students:
            print("No students available")
            return
        print("List of students")
        for s in self.__students:
            print(f"ID: {s.get_id()}, Name: {s.get_name()}, DoB: {s.get_dob()}")
    def dis_course (self):
        if not self.__courses:
            print("No courses available")
            return
        print("List of courses")
        for c in self.__courses:
            print(f"Course ID: {c.get_id()}, Name: {c.get_name()}")
    # management
    def add_std (self):
        n = input("Enter number students want to add")
        # //// ????
        student = self.inp_std()
        for s in self.__students:
            if s.get_id() == student.get_id():
                print(f"Student ID {student.get_id()} already exists")
                return
        self.__students.append(student)
        print(f"Add {student.get_name()} successfully")
    def add_course (self):
        course = self.inp_course()
        for c in self.__courses:
            if c.get_id() == course.get_id():
                print(f"Course ID {course.get_id()} already exists")
                return
        self.__courses.append(course)
        print(f"Add {course.get_name()} successfully")
mm = Management()
while True:
    print("0. Exist")
    print("1. Enter Students")
    print("2. Enter Courses")
    print("3. Enter Marks")
    print("4. Display Students")
    print("5. Display Courses")
    print("6. Display Marks")
    choice = int(input("Choice: "))
    if (choice == 0):
        print("Exist...")
        break
    elif (choice == 1):
        print("Enter Students \n")
        mm.add_std()
    elif (choice == 2):
        print("Enter Courses \n")
        mm.add_course()
    # elif (choice == 3):
    #     print("Enter Marks \n")
    #     mm.inputMarks()
    elif (choice == 4):
        print("Display Students \n")
        mm.dis_std()
    elif (choice == 5):
        print("Display Courses \n")
        mm.dis_course()
    # elif (choice == 6):
    #     print("Display Marks \n")
    #     mm.displayMarks()
    else:
        print("Invalid choices \n")
        continue