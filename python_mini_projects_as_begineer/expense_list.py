# question 2: Write a function that takes a list of expenses and returns a dictionary with the total, highest, and average expense.
def expenses(expense_list):
        dict_expense = {
            "Total": sum(expense_list),
            "Highest": max(expense_list),
            "Average": sum(expense_list)/len(expense_list)
        }
        print(dict_expense)
print(expenses([120, 50, 300, 80]) )  