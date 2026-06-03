class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display_student(self):
        print("Roll No:", self.roll_no)

s = Student("Ganesh", 20, 101)

s.display_person()
s.display_student()