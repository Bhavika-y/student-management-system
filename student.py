class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No : {self.roll}")
        print(f"Name    : {self.name}")
        print(f"Marks   : {self.marks}")


students = []


def add_student():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    s = Student(roll, name, marks)
    students.append(s)
    print("Student Added Successfully.")


def display_students():
    if len(students) == 0:
        print("No Student Found.")
    else:
        for s in students:
            s.display()


def search_student():
    roll = int(input("Enter Roll No: "))

    for s in students:
        if s.roll == roll:
            s.display()
            return
    print("Student Not Found.")


def update_student():
    roll = int(input("Enter Roll No: "))

    for s in students:
        if s.roll == roll:
            s.marks = float(input("Enter New Marks: "))
            print("Student Updated Successfully.")
            return
    print("Student Not Found.")


def delete_student():
    roll = int(input("Enter Roll No: "))

    for s in students:
        if s.roll == roll:
            students.remove(s)
            print("Student Deleted Successfully.")
            return
    print("Student Not Found.")


def display_topper():
    if len(students) == 0:
        print("No Student Found.")
        return
    top = students[0]
    for s in students:
        if s.marks > top.marks:
            top = s
    print("\nTopper Details:")
    top.display()