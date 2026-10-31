def calculate_average(marks):
    return sum(marks) / len(marks)

students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]

for student in students:
    roll = student[0]
    name = student[1]
    marks = student[2]
    print(f"{roll} {name}: {calculate_average(marks):.2f}")