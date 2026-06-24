# To do list
todo_list = []
def add_task():
    task = input("Enter the task: ")
    todo_list.append({"Task": task, "Status": "Pending"})
    print("Task added successfully...\n")
def view_tasks():
    print("Your Todo List:")
    if len(todo_list) == 0:
        print("No tasks found.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task['Task']} - {task['Status']}")
def remove_task():
    if len(todo_list) == 0:
        print("No tasks to remove.")
    else:
        try:
            index = int(input("Enter the number of the task to remove: ")) - 1
            if 0 <= index < len(todo_list):
                removed_task = todo_list.pop(index)
                print(f"Task '{removed_task['Task']}' removed successfully.\n")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
def mark_task_completed():
    if len(todo_list) == 0:
        print("No tasks to mark as completed.")
    else:
        try:
            index = int(input("Enter the number of the task to mark as completed: ")) - 1
            if 0 <= index < len(todo_list):
                todo_list[index]["Status"] = "Completed"
                print("Task marked as completed.\n")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
def task():
    while True:
        print("***Main Menu***")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark a Task as Completed")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_task_completed()   
        elif choice == '5':
            print("Exiting...")
            exit()  
        else:
            print("Invalid choice. Please try again.")
task()
            