def add_transaction(transactions):
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")
        return
    types = input("Enter the type (Income/Expense): ").strip().capitalize()
    if types not in ["Income", "Expense"]:
        print("Invalid type. Please enter 'Income' or 'Expense'.")
        return
    if types=="Expense":
        total_income = sum(t['amount'] for t in transactions if t['type'] == 'Income')
        total_expense = sum(t['amount'] for t in transactions if t['type'] == 'Expense')
        if amount > (total_income - total_expense):
            print("Insufficient balance for this expense.")
            return
    category = input("Enter the category Like Food,Salary: ").strip()
    description = input("Enter a description: ").strip()
    transaction = {
        "amount": amount,
        "type": types,
        "category": category,
        "description": description
    }
    transactions.append(transaction)
    print(f"transaction '{types} - {amount}-{category}' added successfully.")
def view_transaction(transactions):
    if transactions:
        print("Transactions:")
        total_income = 0
        total_expense = 0
        for index, transaction in enumerate(transactions, start=1):
            print(f"{index}. {transaction['type']} - {transaction['amount']} - {transaction['category']} - {transaction['description']}")
            if transaction['type'] == 'Income':
                total_income+=transaction['amount']
            else:
                total_expense+=transaction['amount']
        print(f"Total Income: {total_income}")
        print(f"Total Expense: {total_expense}")
        print(f"Net Balance: {total_income - total_expense}")
    else:
        print("No transactions recorded.")
def remove_transaction(transactions):
    if not transactions:
        print("No transactions to remove.")
        return
    view_transaction(transactions)
    choice = input("Enter the transaction number to remove: ")
    if not choice.isdigit():
        print("Invalid input. Please enter a number.")
        return
    choice = int(choice)
    if 1 <= choice <= len(transactions):
        removed_transaction = transactions.pop(choice - 1)
        print(f'Transaction "{removed_transaction["type"]} - {removed_transaction["amount"]}" has been removed.')
def vew_summary_by_category(transactions):
    summary = {}
    for transaction in transactions:
        category = transaction["category"]
        amount = transaction["amount"]
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    print("Summary by Category:")
    for category, total in summary.items():
        print(f"{category}: {total}") 
transactions=[]
while True:
    
    print("\nFinancial Tracker Menu:")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Remove Transaction")
    print("4. View Summary by Category")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_transaction(transactions)
    elif choice == '2':
        view_transaction(transactions)
    elif choice == '3':
        remove_transaction(transactions)
    elif choice == '4':
        vew_summary_by_category(transactions)
    elif choice == '5':
        print("Exiting the Financial Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")                       