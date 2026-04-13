import json
import os

FILE = "students.json"

if not os.path.exists(FILE): # creates json file by default if not created
    with open(FILE,"w") as f:
        json.dump({}, f)

def load_data(): # load data before running code
    with open(FILE,"r") as f:
        data = json.load(f)
        return data  # json stores keys as strings -> convert back to mormal
    
def save_data(data): # saves data after running code
    with open(FILE, "w") as f:
        json.dump(data, f)

def calculate_grade(marks): # grade allocation function
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 35:
        return "D"
    else :
        return "Fail"

student = load_data() # loading before code

print("-------- STUDENT RESULT MANAGER --------") # menu
while True:
    print("----MENU----")
    print("1. Add student")
    print("2. View Students")
    print("3. Check result")
    print("4. Exit")
    print("----------------------------------------")

    choice = input("Enter your choice :")

    if choice == "1":
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        grade = calculate_grade(marks)
        student[id] = [name, marks, grade] 
        save_data(student)
        print("Student successfully added !")
        print("----------------------------------------\n")

    elif choice == "2":
        if not student:
            print("No student found !")
            print("----------------------------------------\n")
        else:
            print(f"{'ID':<10}{'NAME':<20}{'MARKS':<10}{'GRADE':<10}")
            for id, [name, marks, grade] in student.items():
                print(f"{id:<10}{name:<20}{marks:<10}{grade:<10}")
            print("----------------------------------------\n")

    elif choice == "3":
        id = input("Enter student id: ")
        if id in student:
            name, marks, grade = student[id]
            print(f"Name  : {name}")
            print(f"Marks : {marks}")
            print(f"Grade : {grade}")

            if grade != "Fail":
                print(name, "passed !")
            else:
                print(name, "failed !")

            print("----------------------------------------\n")
            
        else:
            print("Student not found !")
            print("----------------------------------------\n")

    elif choice == "4":
        print("Exiting ........")
        save_data(student) # final save
        break

    else:
        print("Invalid input !")
        print("----------------------------------------\n")