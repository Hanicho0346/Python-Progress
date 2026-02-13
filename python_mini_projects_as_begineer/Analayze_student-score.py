def analyze_scores(students):
    valid_students=[]
    average_score=[]
    highest_score=[]
    passed_students=[]
    for student in students:
        name=student.get("name")
        score=student.get("score")
        if not isinstance(score,(int,float)) or score <0 or score>100:
            print(f"Invalid score for student {name}. Skipping.")
            continue
        valid_students.append(name)
        average_score.append(score)
        highest_score.append(score)
        if score>50:
            passed_students.append(name)
    if valid_students:
        average_score=sum(average_score)/len(average_score)
        highest_score=max(highest_score)
        print(f"Average Score: {average_score}")
        print(f"Highest Score: {highest_score}")
        print("Passed Students:")
        for student in passed_students:
            print(f"{student['name']} - {student['score']}")
students=[
    {"name":"Alice","score":85},
    {"name":"Bob","score":45},
    {"name":"Charlie","score":92},
    {"name":"David","score":-10},
    {"name":"Eve","score":110},
    {"name":"Frank","score":"A+"}
]
analyze_scores(students)

        