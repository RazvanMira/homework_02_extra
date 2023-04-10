grade = float(input("Introduce the grade points.\n"))
if grade > 4.0:
    print("A+ letter grade.")
elif grade == 4.0:
    print("A+ or A letter grade.")
elif grade <= 4.0 and grade >= 3.85:
    print("A letter grade.")
elif grade < 3.85 and grade >= 3.5:
    print("A- letter grade")
elif grade < 3.5 and grade >= 3.15:
    print("B+ letter grade")
elif grade < 3.15 and grade >= 2.85:
    print("B letter grade.")
elif grade < 3.85 and grade >= 2.5:
    print("B- letter grade.")
elif grade < 2.5 and grade >= 2.15:
    print("C+ letter grade.")
elif grade < 2.15 and grade >= 1.85:
    print("C letter grade.")
elif grade < 1.85 and grade >= 1.5:
    print("C- letter grade.")
elif grade < 1.5 and grade >= 1.15:
    print("D+ letter grade.")
elif grade < 1.15 and grade >= 0.5:
    print("D letter grade.")
elif grade < 0.5 and grade >= 0:
    print("F letter grade.")
else:
    print("You did not introduce a valid grade.")