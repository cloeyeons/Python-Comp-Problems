price = [12, 10, 7, 5]

for j in range(10):
    total_cost = int(input())
    proportion = input().split()
    total_students = int(input())

    for i in range(len(proportion)):
        proportion[i] = float(proportion[i])   

    grade_students = []

    for p in proportion:
        students = int(total_students * p)
        grade_students.append(students)

    counted = sum(grade_students)
    missing = total_students - counted 
    most_students = max(grade_students)
    where = grade_students.index(most_students)
    grade_students[where] = grade_students[where] + missing

    total_raised = 0
    for i in range(len(grade_students)):
        total_raised = total_raised + grade_students[i] * price[i]

    if total_raised / 2 < total_cost:
        print("YES")
    else:
        print("NO")



