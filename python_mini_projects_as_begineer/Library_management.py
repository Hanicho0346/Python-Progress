from abc import ABC, abstractmethod 
class LibrarayItem(ABC):
    total_items_count = 0
    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        LibrarayItem.total_items_count += 1
    @staticmethod
    def libraray_rules():
        print("Library Rules:")
        print("1. Return items on time.")
        print("2. Handle items with care.")
        print("3. No food or drinks allowed.")
    @classmethod
    def total_items(cls):
        print(f"Total items in the library: {cls.total_items_count}")
    @abstractmethod
    def display_info(self):
        if self.title is None or self.author is None:
            print("Item details are incomplete.")
            return
        else:
            print(f"Title: {self.title}, Author: {self.author}, Borrowed: {self.is_borrowed}")
    def borrow_item(self):
        if self.is_borrowed:
            print(f"{self.title} is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"You have borrowed {self.title}.")
    def return_item(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You have returned {self.title}.")
        else:
            print(f"{self.title} was not borrowed.")
class Book(LibrarayItem):
    def __init__(self, title, author, is_borrowed, pages):
        super().__init__(title, author, is_borrowed)
        self.pages=pages
    def display_info(self):
        print(f"Book Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Borrowed: {self.is_borrowed}")
class Magazine(LibrarayItem):
    def __init__(self, title, author, is_borrowed ,issue_number):
        super().__init__(title, author, is_borrowed)
        self.issue_number=issue_number
    def display_info(self):
        print(f"Magazine Title: {self.title}, Author: {self.author}, Issue Number: {self.issue_number}, Borrowed: {self.is_borrowed}")

# Static method → library rules
LibrarayItem.libraray_rules()

# Create items
book1 = Book("Python 101", "Alice", False, 250)
book2 = Book("Math Basics", "Bob", False, 300)
mag1 = Magazine("Science Today", "Charlie", False, 5)

# List of items → polymorphism
items = [book1, book2, mag1]

for item in items:
    item.display_info()
    item.borrow_item()
    item.display_info()
    item.return_item()
    item.display_info()

# Class method → total items
LibrarayItem.total_items()

