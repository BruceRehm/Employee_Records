__author__ = 'brehm'

""" accept 4 options
show all employees,
add new employees,
delete existing employee,
find employee,
quit or exit
"""

"""
read from console

bonus is read from a comma delimited file.
also do the final note for dict
"""
#Define Dictionary for employees and ages
employee_db = {"Rob" : 39, "Amit" : 33, "Bruce" : 50, "Fred" : 60}

#Set up Show All Employees Function

def show_all(dictionary):
   for key, value in dictionary.items():
       print (key, value)

#Set up Add Employee Function

def add_employee(dictionary):
    employee_db.update({'Phil':55})
    selection = raw_input("Enter New Employee Name: ")
    kinput = selection
    print kinput
    selection = raw_input("Enter New Employee Age: ")
    vinput = selection
    print vinput
    #return selection
    employee_db.update({kinput: vinput})

#Set up Delete Employee Function

def delete_employee(dictionary):
    selection = raw_input("Enter Employee you wish to TERMINATE!: ")
    # return selection
    einput = selection
    selection = raw_input("Are you sure you want to delete? ")
    dinput = selection
    print dinput
    if dinput == "Y":
        del employee_db[einput]

    elif dinput != "Y":
        print "Thanks Anyways"


#Set up Find Employee Function

def find_employee(dictionary):
    selection = raw_input("Enter Employee you wish to Creep on!: ")
    # return selection
    einput = selection
    print einput
    for key, value in dictionary.items():
        if key == einput:
            print (key, value)

#Set up Exit Function

def exit():
    print "exit"

#Main Program

while True:
    def menu_options():
         print "\n"
         print "Welcome to the Employee Database System"
         print "1. Show All Employees" + "\n" + "2. Add New Employee" + "\n" + "3. Delete Existing Employee" + "\n" + "4. Find Employees" + "\n" + "5. Exit Employee Database " + "\n"
         selection = raw_input("Enter a number 1 - 5 ")
         return selection

    user_selection = int(menu_options())
    print "\n"
    print "Your Selection is: ", user_selection
    print "\n"

    if user_selection == 1:
        show_all(employee_db)

    elif user_selection == 2:
        add_employee(employee_db)

    elif user_selection == 3:
        delete_employee(employee_db)

    elif user_selection == 4:
        find_employee(employee_db)

    elif user_selection == 5:
        print "Thank you for using the Employee Database System"
        break

