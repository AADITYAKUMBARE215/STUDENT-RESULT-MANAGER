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

student = load_data() # loading before code

print("-------- STUDENT RESULT MANAGER --------")
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
        student[id] = [name, marks] 
        print("Student successfully added !")
        print("----------------------------------------\n")

    elif choice == "2":
        if not student:
            print("No student found !")
            print("----------------------------------------\n")
        else:
            print(f"{'ID':<10}{'NAME':<20}{'MARKS':<10}")
            for id, [name, marks] in student.items():
                print(f"{id:<10}{name:<20}{marks:<10}")
            print("----------------------------------------\n")

    elif choice == "3":
        id = input("Enter student id: ")
        if id in student:
            name, marks = student[id]
            print ("marks : ",marks)
            if marks >= 40:
                print(name," passed !")
                print("----------------------------------------\n")
            else:
                print(name," failed !")
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