import os
def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            tasks = f.read().splitlines()
    return tasks

def save_tasks(filename, tasks):
    with open(filename, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def display_tasks(tasks):
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty!")

def add_task(tasks, new_task):
    tasks.append(new_task)
    print(f"'{new_task}' has been added to your to-do list.")

def remove_task(tasks, task_index):
    if task_index >= 1 and task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"'{removed_task}' has been removed from your to-do list.")
    else:
        print("Invalid task number. Please enter a valid task number.")

def main():
    filename = "todo.txt"
    tasks = load_tasks(filename)
    while True:
        print("\nOptions:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the task to add: ")
            add_task(tasks, new_task)
        elif choice == '3':
            display_tasks(tasks)
            task_index = int(input("Enter the task number to remove: "))
            remove_task(tasks, task_index)
        elif choice == '4':
            save_tasks(filename, tasks)
            print("Your to-do list has been saved. Goodbye!Have a productive day!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
main()

