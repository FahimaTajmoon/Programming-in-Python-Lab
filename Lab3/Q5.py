marks = float(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 80:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 70:
    print("Grade: A-")
elif marks >= 65:
    print("Grade: B+")
elif marks >= 60:
    print("Grade: B")
elif marks >= 55:
    print("Grade: B-")
elif marks >= 50:
    print("Grade: C+")
elif marks >= 45:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")