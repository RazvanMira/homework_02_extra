letter_grade = input("Introduce the letter grade.\n")
if letter_grade == "A+" or letter_grade == "A":
    print("4.0 grade points")
elif letter_grade == "A-":
    print("3.7 grade points")
elif letter_grade == "B+":
    print("3.3 grade points")
elif letter_grade == "B":
    print("3.0 grade points")
elif letter_grade == "B-":
    print("2.7 grade points")
elif letter_grade == "C+":
    print("2.3 grade points")
elif letter_grade == "C":
    print("2.0 grade points")
elif letter_grade == "C-":
    print("1.7 grade points")
elif letter_grade == "D+":
    print("1.3 grade points")
elif letter_grade == "D":
    print("1.0 grade points.")
elif letter_grade == "F":
    print("0 grade points")
else:
    print("You did not introduce a valid letter grade.")