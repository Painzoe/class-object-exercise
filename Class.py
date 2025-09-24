import os
import sys

class Employees:
    NumOf_employees = 0
    def __init__(self,name,surname,salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        Employees.NumOf_employees += 1

def update_file(filename, employees_list):
    with open(filename,"w",encoding="utf-8") as file:
        for a in range(Employees.NumOf_employees):
            file.write(f"{employees_list[a].name} {employees_list[a].surname} , {employees_list[a].salary}\n")

def read_file(filename,employees_list):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    full_name , salary = line.split(",")
                    name, surname = full_name.split(" ",1) # Divides first hole
                    employee = Employees(name,surname,salary)
                    employees_list.append(employee)
    except FileNotFoundError:
        pass

while True:
    os.system("cls")
    menu = """
    -------------Employees List Menu-------------
    1. Add New Employee Information
    2. Delete the Dismissed Employee Information
    3. View the Employee List
    4. Quit
    """
    print(menu)
    read_file("employees.txt",employees)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter employee name: ")
        surname = input("Enter employee surname: ")
        salary = float(input("Enter employee salary: "))
        full_name = f"{name} {surname}"
        employee = Employees(name,surname,salary)
        employees[full_name] = salary
        update_file("employees.txt",employees)
    elif choice == 2:
        name = input("Enter employee name: ")
        surname = input("Enter employee surname: ")
        full_name = f"{name} {surname}"
        if full_name in employees.keys():
            del employees[full_name]
        update_file("employees.txt",employees)
    elif choice == 3:
        print(employees)
        print(f"Number of Employees:{Employees.NumOf_employees}")
    elif choice == 4:
        sys.exit()
    else:
        print("Invalid choice")
    enter = input("Press the enter to continue...")





