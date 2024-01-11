import employee_information
import save_file

save_data = save_file.Excel_Save("employee_list.xlsx")

while True:
    try:
        choice = int(input("""Please select the action you want to perform:
        1-Add New Developer
        2-Add New Manager
        3-Get Employee Information
        4-Get The Entire Employee List
        5-Salary Increase
        6-Delete Registration
        7-Exit
        """
            "Enter chocie: "))

        if choice == 1:
            id = input("Enter Id: ")
            name = input("Enter Name: ")
            surname = input("Enter Surname: ")
            salary = input("Enter Salary: ")
            programming = input("Enter Program: ")

            employee = employee_information.Developer(id,name,surname,salary,programming)

            new_data = employee.employee_list() 
            save_data.add_data(new_data)
            print("\n-----New employee added-----\n")       
        
        if choice == 2:
            id = input("Enter Id: ")
            name = input("Enter Name: ")
            surname = input("Enter Surname: ")
            salary = input("Enter Salary: ")

            employee = employee_information.Manager(id,name,surname,salary)

            new_data = employee.employee_list() 
            save_data.add_data(new_data)
            print("\n-----New employee added-----\n")

        if choice == 3:
            target_id = input("Please enter id no: ") 
            row_data = save_data.get_row_by_id(target_id)
            print("\n-----Employee information-----\n",row_data,"\n")
            
        if choice == 4:
            list = save_data.get_all_data()
            print("\n-----All registered employees-----\n",list,"\n")

        if choice == 5: 
            target_id = input("Please enter id no: ")
            new_salary = input("Please enter new salary: ")
            save_data.update_salary_by_id(target_id, new_salary)
            print("\nNew salary successfully updated\n")
          
        if choice == 6:
            target_id = input("Please enter id no: ")
            save_data.delete_row_by_id(target_id)
            print("\nRemoved from the list\n")

        if choice == 7:
            break

    except ValueError:
        print("\nPlease try again\n")