# Author: Andrew Bittner
# Date: 11/10/2024


# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.

class Employee:
    def __init__(self, name, id, dept, job):
        self.__name = name
        self.__id = id
        self.__dept = dept
        self.__job = job
    def __str__(self):
        return f'{self.__name}\n{self.__id}\n{self.__dept}\n{self.__job}\n'

def exit_sequence():
    # Function to keep console/window open until user ends program.
    input('\n\nPress [enter] to exit... ')

def main():
    employee_records = [['Susan Meyers', 47899, 'Accounting', 'Vice President'], ['Mark Jones', 39119, 'IT', 'Programmer'], ['Joy Rogers', 81774, 'Manufacturing', 'Engineer']]
    employee_objects = []
    for employee_info in employee_records:
        employee_objects.append(Employee(employee_info[0], employee_info[1], employee_info[2], employee_info[3]))
    for ind in range(len(employee_objects)):
        print(employee_objects[ind])
    exit_sequence()

if __name__ == '__main__':
    main()