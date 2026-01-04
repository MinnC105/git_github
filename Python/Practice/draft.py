import math as m
import numpy as np
class Student():
    def __init__ (self):
        self.__name = ""
        self.__id = ""
        self.__dob = ""
        self.__gpa = 0.0      
    def input(self):
        self.__name = input("Student name: ")
        self.__id = input("Student id: ")
        self.__dob = input("Student dob: ")
    def display(self):
        print(f"Student: {self.__name} ID: {self.__id} DoB: {self.__dob} GPA: {self.__gpa: .2f}")
class Course():
    def __init__ (self):
        self.__name = ""
        self.__id = ""
        self.__credits = 0    
    def input(self):
        self.__name = input("Course name: ")
        self.__id = input("Course id: ")
        self.__credits = int(input("Course credits: "))
    def display(self):
        print(f"Course: {self.__name} ID: {self.__id} Credits: {self.__credits}")

class Mark():
    def __init__ (self):
        self.__sid = ""
        self.__cid = ""
        self.__mark = 0
    def input (self):
        mark_input = float(input())
        self.__mark = m.floor(mark_input * 10) / 10
    def display(self):
        print(f"Student: {self.__sid} Course: {self.__cid} Mark: {self.__mark}")


def average_gpa (marks_list, credits_list):
    if not marks_list or not credits_list:
        return 0.0
    marks = np.array(marks_list)
    credits = np.array(credits_list)
    weighted_sum = np.sum(marks * credits)
    if np.sum(credits) > 0:
        return weighted_sum / np.sum(credits)
    return 0.0
class gpa_student:
    def __init__ (self, sid, marks, courses):
        self.__sid = sid
        self.__marks = marks
        self.__courses = courses
    def cal (self):
        marks_list = []
        credits_list = []
        for mark in self.marks:
            for course in self.courses:
                if course.id == mark.cid:
                    marks_list.append(mark.mark)
                    credits_list.append(course.credits)
                    break
        return average_gpa (marks_list, credits_list)
class MarkManagement():
    def __init__ (self):
        self.__students = []
        self.__courses = []
        self.__marks = []
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
        check = any(c.id == cid for c in self.courses)  
        if not check:
            print("Course not found")
            return
        for s in self.students:
            print(f"Enter mark for: {s.name} ID: {s.id}")
            mark = Mark()
            mark.sid = s.id
            mark.cid = cid
            print(f"Mark for {s.name}")
            mark.input()
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
while True:
    print("0. Exist \n1. Enter Students \n2. Enter Courses \n3. Enter Marks \n" \
    "4. Display Students \n5. Display Courses \n6. Display Marks \n")
    choice = int(input("Choice: "))
    if (choice == 0):
        print("Exist...")
        break
    elif (choice == 1):
        print("Enter Students \n")
        mm.inputStudents()
    elif (choice == 2):
        print("Enter Courses \n")
        mm.inputCourses()
    elif (choice == 3):
        print("Enter Marks \n")
        mm.inputMarks()
    elif (choice == 4):
        print("Display Students \n")
        mm.displayStudents()
    elif (choice == 5):
        print("Display Courses \n")
        mm.displayCourses()
    elif (choice == 6):
        print("Display Marks \n")
        mm.displayMarks()
    else:
        print("Invalid choices \n")
        continue
