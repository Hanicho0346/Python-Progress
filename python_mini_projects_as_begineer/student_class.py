class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old and I am in grade {self.grade}.")


student1 = Student("Alice", 15, "10th")
student2 = Student("Bob", 16, "11th")

student1.introduce()
student2.introduce()
