class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]
    def deposit(self,amount,description):
       self.ledger.append({"amount":amount,"description":description})
       return self.ledger
    def withdraw(self,amount,description):
        self.ledger.append({"amount":-amount,"description":description})
        return self.ledger
    def check_balance(self):
        total=0
        for item in self.ledger:
            total+=item["amount"]
        return total
    def check_fund(self,amount):
        if amount <=self.check_balance():
            return True
        else:
            return False
    def transfer(self,amount,category):
        if self.check_fund(amount) == False:
            return "Transfer failed: Insufficient funds"
        self.withdraw(amount,f"Transfer to {category.name}")
        category.deposit(amount,f"Transfer from {self.name}")  
        return f"Transfer of {amount} to {category.name} successful"  
        

food=Category("Food")
print(food.name)
print(food.ledger)
print(food.deposit(130,"initial"))  
print(food.withdraw(20,"initial withdraw"))   
print(food.check_balance())  
print(food.check_fund(100)) 
clothing=Category("Clothing")
print(clothing.name)
print(clothing.ledger)

print(clothing.deposit(100,"initial"))
print(clothing.withdraw(20,"initial withdraw"))
print(clothing.check_balance())
print(clothing.check_fund(100))
print(food.transfer(10,clothing))