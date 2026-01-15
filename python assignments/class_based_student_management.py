class Student:
    def __init__(self, roll, name, age, course):
        self.roll = roll
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"Roll: {self.roll}, Name: {self.name}, Age: {self.age}, Course: {self.course}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, roll, name, age, course):
        student = Student(roll, name, age, course)
        self.students.append(student)
        print("✅ Student Added Successfully")

    def view_students(self):
        if not self.students:
            print("⚠ No Students Found")
            return
        for student in self.students:
            student.display()

    def search_student(self, roll):
        for student in self.students:
            if student.roll == roll:
                print("🎯 Student Found:")
                student.display()
                return
        print("❌ Student Not Found")

    def update_student(self, roll, name, age, course):
        for student in self.students:
            if student.roll == roll:
                student.name = name
                student.age = age
                student.course = course
                print("🔄 Student Updated Successfully")
                return
        print("❌ Student Not Found")

    def delete_student(self, roll):
        for student in self.students:
            if student.roll == roll:
                self.students.remove(student)
                print("🗑 Student Deleted Successfully")
                return
        print("❌ Student Not Found")
