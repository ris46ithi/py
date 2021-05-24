
database = {"indira" : 100,
            "gayathri" : 96,
            "mugundhan" : 97,
            "prasanth" : 98,
            "zubair" : 99}

def get_employee_id(employee_name):

    # This statement is to collect the employee names from the dictionary
    employees_name_list = database.keys()

    print ("Employee names presents are : ", employees_name_list)

    # This statement is to check whether the user entered username is available in the dictionary or not
    if employee_name in employees_name_list:
        return database[employee_name]
    else:
        return False


def main():
    user_input = input("Enter a employee name to get the id : ")
    result = get_employee_id(user_input)
    if result == False:
        print ("Given employee name is not available")
    else:
        print ("Employee ID is : ", result)


main()