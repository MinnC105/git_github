import curses
from input import InputSystem 
from output import show_students, show_courses 

from storage import decompress_data, load_students, load_courses, load_marks
from storage import compress_data


class CursesUI:
    def __init__(self, stdscr, students, courses, marks):
        self.stdscr = stdscr
        self.current = 0   

        self.students = students
        self.courses = courses
        self.marks = marks

        self.inputSystem = InputSystem(
            self.stdscr, self.students, self.courses, self.marks
        )
        
        self.menu = [
            "Add students",
            "Add courses",
            "Add marks",
            "Show students + GPA",
            "Show courses",
            "Exit"
        ]

    def draw_menu(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 2, "STUDENT MANAGEMENT (CURSES)", curses.A_BOLD)
        for i, item in enumerate(self.menu):
            if i == self.current:
                self.stdscr.addstr(i + 2, 4, item, curses.A_REVERSE)
            else:
                self.stdscr.addstr(i + 2, 4, item)
        self.stdscr.refresh()

    def run(self):
        curses.curs_set(0)        
        self.stdscr.keypad(True)    

        while True:
            self.draw_menu()
            key = self.stdscr.getch()

            if key == curses.KEY_UP and self.current > 0:
                self.current -= 1
            elif key == curses.KEY_DOWN and self.current < len(self.menu) - 1:
                self.current += 1
            elif key in (10, 13):
                if self.current == 0:
                    self.inputSystem.input_students()
                elif self.current == 1:
                    self.inputSystem.input_courses()
                elif self.current == 2:
                    self.inputSystem.input_marks()
                elif self.current == 3:
                    show_students(self.stdscr, self.students, self.courses, self.marks)
                elif self.current == 4:
                    show_courses(self.stdscr, self.courses)
                elif self.current == 5:
                    compress_data()
                    break

def main(stdscr):
    students, courses, marks = [], [], []

    if decompress_data():
        students = load_students()
        courses = load_courses()
        marks = load_marks()

    ui = CursesUI(stdscr, students, courses, marks)
    ui.run()

curses.wrapper(main)
