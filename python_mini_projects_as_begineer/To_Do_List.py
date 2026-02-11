def add_item(my_list):
    task = input("Enter the item to add: ")

    for item in my_list:
        if item["task"] == task:
            print(f'"{task}" is already in the list.')
            return

    my_list.append({
        "task": task,
        "Completed": False
    })
    print(f'"{task}" has been added to the list.')


def remove_item(my_list):
    if not my_list:
        print("The list is empty.")
        return

    task = input("Enter the item number to remove: ")
    if not task.isdigit():
        print("Invalid input. Please enter a valid item number.")
        return

    task = int(task)
    if 1 <= task <= len(my_list):
        removed_item = my_list.pop(task - 1)
        print(f'"{removed_item["task"]}" has been removed from the list.')
    else:
        print("Invalid item number.")


def view_list(my_list):
    if my_list:
        print("Current List:")
        for index, task in enumerate(my_list, start=1):
            status = "✔️" if task["Completed"] else "❌"
            print(f"{index}. {task['task']} - {status}")
    else:
        print("The list is currently empty.")


def mark_completed(my_list):
    if not my_list:
        print("No tasks to mark as completed.")
        return

    view_list(my_list)
    choice = input("Enter the item number to mark as completed: ")

    if not choice.isdigit():
        print("Invalid input. Please enter a number.")
        return

    choice = int(choice)
    if 1 <= choice <= len(my_list):
        my_list[choice - 1]["Completed"] = True
        print(f'Task "{my_list[choice - 1]["task"]}" marked as completed ✔️')
    else:
        print("Invalid item number.")



playing = True
my_list = []

while playing:
    print("\n--- To-Do List Manager ---")
    print("==========================")
    print("1. Add to List")
    print("2. View List")
    print("3. Remove from List")
    print("4. Mark task as Completed")
    print("5. Exit")
    print("==========================")

    user_choice = input("Enter the number of your choice: ")

    if user_choice == "1":
        add_item(my_list)
    elif user_choice == "2":
        view_list(my_list)
    elif user_choice == "3":
        remove_item(my_list)
    elif user_choice == "4":
        mark_completed(my_list)
    elif user_choice == "5":
        playing = False
        print("Exiting the List Manager. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
