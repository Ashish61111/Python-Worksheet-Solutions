students = {
    "Ashish": {"Marks": 85, "Grade": "A"},
    "Rahul": {"Marks": 78, "Grade": "B"},
    "Priya": {"Marks": 92, "Grade": "A"},
    "Sneha": {"Marks": 88, "Grade": "A"},
    "Kiran": {"Marks": 75, "Grade": "B"}
}

print("Student Details:")
for name, details in students.items():
    print("Name:", name)
    print("Marks:", details["Marks"])
    print("Grade:", details["Grade"])
    print()

highest_student = max(students, key=lambda x: students[x]["Marks"])

print("Student with Highest Marks:")
print("Name:", highest_student)
print("Marks:", students[highest_student]["Marks"])
print("Grade:", students[highest_student]["Grade"])