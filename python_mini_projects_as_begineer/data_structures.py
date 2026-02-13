class Stack:
    def __init__(self):
        self.stack=[]
    def push(self, item):
        self.stack.append(item)
        print(f"Item '{item}' pushed to stack.")
    def pop(self):
        self.stack.pop()
        print("Item popped from stack.")
    def peek(self):
        top_item=self.stack[-1]
        print(f"Top item in stack: '{top_item}'.")
    def is_empty(self):
        if len(self.stack)==0:
            print("Stack is empty.")
        else:
            print("Stack is not empty.")
item=Stack()
item.push(10)
 
item.push(20)
print("stack data",item.stack)  
item.peek() 
item.pop()
print("stack data",item.stack)  
item.is_empty()
item.pop()
  
item.is_empty()
print()


class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Item '{item}' added to queue.")
    def dequeue(self):
        self.queue.pop(0)
        print("Item removed from queue.")
    def front(self):
        front_item=self.queue[0]
        print(f"Front item in queue: '{front_item}'.")
print()
queue=Queue()
queue.enqueue(10)
print("queue data",queue.queue)
queue.enqueue(20)
print("queue data",queue.queue)
queue.front()
queue.dequeue()
print("queue data",queue.queue)


class LinkedListNode:
    def __init__(self, data):
        self.data=data
        self.next=None
    def append(self, data):
        new_node=LinkedListNode(data)
        current=self
        while current.next:
            current=current.next
        current.next=new_node
    def display(self):
        current=self
        while current:
            print(current.data, end=" -> ")
            current=current.next
        print("None")

print()
linked_list=LinkedListNode(10)
linked_list.append(20)
linked_list.append(30)
print("Linked List data: ", end="")
linked_list.display()
