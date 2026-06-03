file = open("students.txt", "w")

file.write("Ashish\n")
file.write("Rahul\n")
file.write("Priya\n")
file.write("Sneha\n")
file.write("Kiran\n")

file.close()

file = open("students.txt", "r")

print("Student Names:")
names = file.readlines()

for name in names:
    print(name.strip())

file.close()

count = len(names)

print("\nTotal Number of Students:", count)