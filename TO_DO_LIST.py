todo_list = []
def show_tasks():
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task(task):
    todo_list.append(task)
    print('Task added to the list.')

def delete_task(index):
    if 0 < index <= len(todo_list):
        removed_task = todo_list.pop(index - 1)
        print(f"Deleted: {removed_task}")
    else:
        print("Invalid task number.")

while True:
    print("\n===To-Do List Menu:===")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '3':
        show_tasks()
        try:
            idx = int(input("Enter the task number to delete: "))
            delete_task(idx)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '4':
        print("Sorry to see you go! Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")