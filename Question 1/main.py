import numpy as np

print("Welcome to course registration !")
while True:
    Student_Name = input("Enter your name : ")
    Roll_No = input("Enter your Roll number : ")
    Current_Sem = int(input("Current Semester (*integer) : "))
    response = input("Are you sure ? (y/n) : ")
    if response == 'y' or response == 'Y':
        break

Year = int(Current_Sem / 2) + 1
Opted = []
avail = []

Courses = np.genfromtxt('courses%d.txt' % (Current_Sem % 2), dtype=None, delimiter=',', encoding=None)

for course in Courses:
    if course[0][0] in (Roll_No[0], "H", "S") and course[0][2] == str(Year):
        avail.append(course)

print("\nCourses available -")
for index, value in enumerate(avail):
    print(index + 1, "-", value[0], value[1])

while True:
    total = int(input("How many courses you want to opt for : "))
    while total < 4 or total > 7:
        print("You must Choose between 4 to 7 courses !")
        total = int(input("Number of courses : "))

    print("Give corresponding index of courses :")

    for i in range(0, total):
        idx = int(input())
        Opted.append(avail[idx - 1])
        print(avail[idx - 1][0], " selected !")

    print("You're opting for : ")
    for i in Opted:
        print(i[0], i[1])

    response = input("Are you sure ? (y/n) : ")
    if response == 'y' or response == 'Y':
        break
    else:
        Opted.clear()

File = open(r'student course information.txt', 'a')
string = Roll_No + "," + Student_Name + "," + str(Current_Sem) + "," + ",".join(['-'.join(ele) for ele in Opted]) + "\n"
File.write(string)
print("\nCourse Registration Successful !")
