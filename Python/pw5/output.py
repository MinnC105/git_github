import numpy as np

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
- self tồn tại trong method của class
- trong function bình thường không cần, cần nạp đủ tham số
- InputSystem bắt buộc là CLASS, vì: 
    - cần giữ state lâu dài
    - Output không cần vì chỉ cần hiển thị (dùng function cho basic)
"""
def show_students(stdscr, students, courses, marks):
        stdscr.clear()
        
        data = [] 
        for s in students:
            gpa = cal_gpa(s, courses, marks)
            data.append((s, gpa)) 
        data.sort(key = lambda x: x[1], reverse = True)

        y = 2 
        for s, gpa in data:
            stdscr.addstr(y, 2, f"{s.get_sid()} | {s.get_name()} | GPA: {gpa:.2f}")
            y += 1
        stdscr.getch()

def show_courses(stdscr, courses):
    stdscr.clear()
    y = 2
    for c in courses:
        stdscr.addstr(y, 2, f"{c.get_cid()} | {c.get_name()} | {c.get_credit()}")
        y += 1
    stdscr.getch()
