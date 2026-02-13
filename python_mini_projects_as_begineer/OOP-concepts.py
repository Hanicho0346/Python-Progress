class Employee:
    def __init__(self):
        self.name = None
        self.department = None
        self.salary = 0

    def get_details(self):
        if self.name is None or self.department is None:
            print("Employee details are incomplete.")
            return
        print(f"Employee Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary}")

    def calculate_bonus(self, bonus_percentage=10):
        if self.salary == 0:
            print("Cannot calculate bonus for an employee with no salary.")
            return 0
        bonus = (self.salary * bonus_percentage) / 100
        return bonus  




class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.team_size = 0

    def calculate_bonus(self, bonus_percentage=20):
        base_bonus = super().calculate_bonus(bonus_percentage)
        extra_bonus = 100 * self.team_size
        total_bonus = base_bonus + extra_bonus
        return total_bonus


class Developer(Employee):
    def __init__(self):
        super().__init__()
        self.programming_languages = []

    def calculate_bonus(self, bonus_percentage=15):
        total_bonus = super().calculate_bonus(bonus_percentage)
        return total_bonus



emp1=Employee()
emp1.name="Alice"
emp1.department="HR"
emp1.salary=50000
emp2=Manager()
emp2.name="Bob"
emp2.department="IT"
emp2.salary=80000
emp2.team_size=5
emp3=Developer()
emp3.name="Charlie"
emp3.department="Software"
emp3.salary=70000
emp3.programming_languages=["Python","JavaScript"]
employees = [emp1, emp2, emp3]

for emp in employees:
    emp.get_details()
    bonus = emp.calculate_bonus()
    print(f"Bonus for {emp.name}: ${bonus}\n")



    
       