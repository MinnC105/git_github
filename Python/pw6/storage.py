import os
import zipfile
from domains import Student, Course, Mark

ARCHIVE = "students.dat"
FILES = ["students.txt", "courses.txt", "marks.txt"]


def compress_data():
    with zipfile.ZipFile(ARCHIVE, "w", zipfile.ZIP_DEFLATED) as z:
        for file in FILES:
            if os.path.exists(file):
                z.write(file)


def decompress_data():
    if not os.path.exists(ARCHIVE):
        return False

    with zipfile.ZipFile(ARCHIVE, "r") as z:
        z.extractall()

    return True


def load_students():
    students = []
    if not os.path.exists("students.txt"):
        return students

    with open("students.txt") as f:
        for line in f:
            sid, name, dob = line.strip().split("|")
            students.append(Student(sid, name, dob))
    return students

def load_courses():
    courses = []
    if not os.path.exists("courses.txt"):
        return courses

    with open("courses.txt") as f:
        for line in f:
            cid, name, credit = line.strip().split("|")
            courses.append(Course(cid, name, int(credit)))
    return courses

def load_marks():
    marks = []
    if not os.path.exists("marks.txt"):
        return marks

    with open("marks.txt") as f:
        for line in f:
            sid, cid, mark = line.strip().split("|")
            marks.append(Mark(sid, cid, float(mark)))
    return marks

