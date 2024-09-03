def get_grade(grade1, grade2, grade3):
    average = sum([grade1, grade2, grade3]) / 3
    if average < 60:
        return 'F'
    elif average < 70:
        return 'D'
    elif average < 80:
        return 'C'
    elif average < 90:
        return 'B'
    elif average <= 100:
        return 'A'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True