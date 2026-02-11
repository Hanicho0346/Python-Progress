# question 10:Shopping List Manager

def shopping_list_manager():
    shopping_list = []
    while True:
        print("\nShopping List Manager")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)

        elif choice == "4":
            print("Exiting the Shopping List Manager. Goodbye!")
            break

def add_item(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")
def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.") 
def view_list(shopping_list):
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("Your shopping list:")
        for item in shopping_list:
            print(f"- {item}")

shopping_list_manager()  