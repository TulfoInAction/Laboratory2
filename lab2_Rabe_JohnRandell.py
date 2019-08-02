studentlist = []

class Employees:
    def __init__(self, name, department, position, rate):
        self.name = name
        self.department = department
        self.position = position
        self.rate = rate
        
        

    def getSalary(self, rate, hour):
        return self.rate * hour

program = True

while program:
    print('''**********
Choose your Option
**********
1. Add new Employee
2. Enter Hourly of Employee
3. Show Employees Information
4. Exit
***********''')

    print("\n Please enter your option. ", end ="")
    ans = int(input())

    if ans == 1:
        print("Please add employee: ", end = "")
        name = input()
        print("Please add department: ", end = "")
        department = input()
        print("Please add position: ", end = "")
        position = input()
        print("Please add rate: ", end = "")
        rate = int(input())
        studentlist.append(Employees(name, department, position, rate))
        
    if ans == 2:
        x = int(input("Enter the index of your Employee: "))
        salary = studentlist[x]
        hour = int(input("Enter Hourly: "))
        print(salary.getSalary(rate, hour))
        
        
        
    if ans == 3:
        for x in studentlist:
            print("ID: ", studentlist.index(x), "\nNAME: ", x.name, "\nDEPARTMENT: ", x.department, "\nPOSITION: ", x.position, "\nRATE: ", x.rate)
            

    if ans == 4:
        print('Areou want to exit? Y/N? ')
        x = input()

        if x == "y":
            print('Goodbye. SEE YOU SOON! ')
            program = False

        else:
            continue
    
   
        
