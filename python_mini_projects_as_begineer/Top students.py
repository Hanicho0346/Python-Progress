# question 11:Top students

students = [
    {'name': 'Alice', 'grades': [90, 80, 85]},
    {'name': 'Bob', 'grades': [70, 95, 88]},
    {'name': 'Charlie', 'grades': [100, 100, 100]}
]

top_student = max(students, key=lambda s: sum(s['grades'])/len(s['grades']))


average = sum(top_student['grades']) / len(top_student['grades'])
print(f"Top student: {top_student['name']} with average {average}")
