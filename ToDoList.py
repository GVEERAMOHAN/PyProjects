# create a empty list
todo_list = []

# create add feature in todolist application
def add_list():
    task = input("Enter the Task: ")
    todo_list.append({'Task': task, 'Status': "pending"})
    print("The task has been added successfully!\n")

# create view feature in todolist application
def view_list():
    print("Your list is: ")
    if len(todo_list) == 0:
        print("The list is empty!")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print("")

# create remove feature in todolist application
def remove_list():
    try:
        if len(todo_list) == 0:
            print("The list is empty!")
        else:
            search_index = int(input("Enter the task number to be removed: ")) - 1
            if 0 <= search_index < len(todo_list):
                removed_list = todo_list.pop(search_index)
                print(f"Task Removed: {removed_list['Task']}")
            else:
                print("Invalid task.")
    except ValueError:
        return "Invalid Task"
    print("")

# create mark feature in todolist application
def mark_list():
    try:
        if len(todo_list) == 0:
            print("The list is empty!")
        else:
            search_index = int(input("Enter the task number to be marked as done: ")) - 1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]['Status'] = 'done'
                print(f"The '{search_index + 1}' task is marked as done!")
            else:
                print("Invalid task.")
    except ValueError:
        return "Invalid Task"
    print("")   

# create menu in todolist application
def menu():
    while True:
        print("<----Main Menu---->")
        print("1. Add new Task.")
        print("2, View all Tasks.")
        print("3. Remove a Task.")
        print("4. Mark a Task.")
        print("5. Exit...")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_list()
        elif choice == "2":
            view_list()
        elif choice == "3":
            remove_list()
        elif choice == "4":
            mark_list()
        elif choice == "5":
            print("Exiting the application....")
            exit()

# print statement
menu()