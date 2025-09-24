import os
import sys

class Employees():
    NumOf_employees = 0
    def __init__(self,name,surname,salary,department,phone_num):
        self.name = name
        self.surname = surname
        self.salary = float(salary)
        self.department = department
        self.phone_num = phone_num
        Employees.NumOf_employees += 1


menu = """
           Employee Information List
1. Add a new employee information
2. Remove the dismissed employee from the list
3. Display the list of employees
4. Quit

"""

def update_file (employees_list):
        with open('employees.txt', 'w',encoding="utf-8") as file:
            for employee in employees_list:
                file.write(f"{employee.name},{employee.surname},{employee.salary},{employee.department},{employee.phone_num}\n")

def read_file (employees_list):
    try:

        with open('employees.txt', 'r', encoding="utf-8") as file:
            for employee in file:
                emp_name , emp_surname, emp_salary, emp_department, emp_phonenum = employee.strip().split(',')
                emp = Employees(emp_name,emp_surname,emp_salary,emp_department,emp_phonenum)
                employees_list.append(emp)
        return employees_list
    except FileNotFoundError:
        pass

employees = list()
read_file(employees)

while True:
    os.system('cls')
    print(menu)
    choice = input("Choose an option(1, 2, 3 or 4): ")
    if choice == '1':
        name = input("Enter employee name: ")
        surname = input("Enter employee surname: ")
        salary = float(input("Enter employee salary: "))
        department = input("Enter employee department: ")
        number = input("Enter employee phone number: ")
        employees.append(Employees(name,surname,salary,department,number))
        print("Employee information added successfully!")
        input("Press enter to return to main menu...")
        update_file(employees)
    elif choice == '2':
        FoundEmp = None
        print("Name and Surname of employee who was dismissed.")
        EName = input("Enter employee name: ")
        ESurname = input("Enter employee surname: ")
        FullNamelist = [f"{a.name} {a.surname}" for a in employees]
        if f"{EName} {ESurname}" in FullNamelist:
            for emp in employees:
                if emp.name == EName and emp.surname == ESurname:
                    FoundEmp = emp
                    break
        if FoundEmp:
            employees.remove(FoundEmp)
            print("Employee information removed successfully!")
            update_file(employees)
        else:
            print("Employee information not found.")
    elif choice == '3':
        print("Updated Employee Information List:")
        with open('employees.txt', 'r',encoding="utf-8") as file:
            for employee in file:
                cleanedLine = employee.strip()
                print(f"{cleanedLine}")
    elif choice == '4':
        sys.exit()
    else:
        print("Invalid choice.")
        input("Press enter to return to main menu...")


