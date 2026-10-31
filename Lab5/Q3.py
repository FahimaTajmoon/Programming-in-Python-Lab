def calculate_average(marks):
    return sum(marks) / len(marks)

def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"

def display_report(students):
    for student in students:
        average = calculate_average(student[2])
        category = classify_performance(average)
        print(f"ID: {student[0]}, Name: {student[1]}, Average: {average:.2f}, Performance: {category}")

students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]

display_report(students)