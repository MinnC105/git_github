students = []
courses = []
marks = {} 

def inp_s():
    n = int(input("Enter number of students: "))
    for i in range(n):
        print(f"Student {i + 1}")
        sid = input("Student ID: ")
        sname = input("Name: ")
        dob = input("Date of Birth: ")
        students.append({
            "id": sid,
            "name": sname,
            "dob": dob
        })

def inp_c():
    m = int(input("Enter number of course: "))
    for i in range(m):
        print(f"Course {i + 1}")
        cid = input("Course ID: ")
        cname = input("Course name: ")
        courses.append({
            "id": cid,
            "name": cname
        })
        marks[cid] = {}

# Select a course, input marks for student in this course
def inp_m():
    print("Select course: ")
    res = input("Course ID want to choose: ")
    for c in courses:
        if res == c["id"]:
            for s in students:        
                mark = float(input(f"Enter mark for {s["name"]}: "))
                marks[c["id"]][s["id"]] = mark 
            return


def list_s():
    print("STUDENT LIST")
    for s in students:
        print(f"{s["id"]}|{s["name"]}|{s["dob"]}")

def list_c():
    print("COURSE LIST")
    for c in courses:
        print(f"{c["id"]}|{c["name"]}")

def list_marks():
    print("Select course: ")
    res = input("Course name want to choose: ")
    for c in courses:
        if res == c["id"]:
            print(f"{res} marks")
            for s in students:
                mark = marks[c["id"]].get(s["id"], "None")
                print(f"{s["name"]}: {mark}") 
            return

inp_s()
inp_c()

while True:
    print("""
        1. Input marks for a course
        2. List students
        3. List courses
        4. Show marks by course
        0. Exit
        """)
    
    choice = input("Choose: ")

    if choice == "1":
        inp_m()

    elif choice == "2":
        list_s()

    elif choice == "3":
        list_c()

    elif choice == "4":
        list_marks()

    elif choice == "0":
        print("Exist ...")
        break
    
    else:
        print("Invalid choice!")
# List
# Courses: ID|name
# Students: ID|name|dob
# Mark (choose 1 subject: marks) name: mark
