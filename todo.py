tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("enter the task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == '2':
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == '3':
            print("tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            remove = input("enter the task for remove: ")
            if remove in tasks:
                tasks.remove(remove)
                print("Task removed successfully.")
            else:
                print("Task not found.")

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
         print("Invalid choice. Please try again.")