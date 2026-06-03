class Student:

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
        print()

student1 = Student("Ashish", 101, 85)
student2 = Student("Rahul", 102, 92)

student1.display_details()
student2.display_details()