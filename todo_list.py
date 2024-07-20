# To-Do List Application
# Functions: 1)Add Tasks 2)View Tasks 3)Delete Tasks by Index Number
# Use list() data struct
# use functions

#function to add a task
def add_a_task(tasks):
    task= input("Enter the new task's name: ")
    tasks.append(task)
    print("New task successfully added!")
    return tasks

#function to display all tasks
def view_all_tasks(tasks):
    if not tasks:
        print("There are no tasks assigned yet. Please add a new task by choosing the other option.")
    else:
        print("Following are the list of tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"Task ID: {i}, Task Name: {task}")

#function to remove a task
def rem_a_task(tasks):
    if not tasks:
        print("There are no tasks to delete. Please add a new task first.")
        return tasks
    try:
        index = int(input("Enter the task ID of the task to delete: "))
        task = tasks.pop(index - 1)
        print("Task deletion successful! Name of the deleted task: ", task)
        return tasks
    except (IndexError, ValueError):
        print("Invalid task ID! Please enter a valid number.")
        return tasks

#Main function for the to-do list application
def main():
    print("----------Welcome to our CLI To-Do List Tool----------\n")
    tasks = []

    while True:
        print("\n1) Add a new task\n2) View all tasks\n3) Delete a task by its index number\n4) Exit")
        try:
            choice = int(input("Enter your option number: "))
            if choice not in (1, 2, 3,4):
                raise ValueError("Invalid option. Please enter a number between 1 and 4.")
        except ValueError as e:
            print(e)
            continue

        if choice == 1:
            tasks = add_a_task(tasks)
        elif choice == 2:
            view_all_tasks(tasks)
        elif choice == 3:
            tasks = rem_a_task(tasks)
        elif choice== 4:
            print("Exiting the to-do application! Hope you have a nice day ahead.")
            break
        else:
            print("Incorrect option!")

if __name__ == "__main__":
    main()

