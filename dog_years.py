print("This programme converts human years to dog years.")
human_years = float(input("Introduce the number of human years.\n"))
if human_years < 0:
    print("Error. You introduced a negative number.")
elif human_years >= 0 and human_years <= 2:
    dog_years = human_years * 10.5
    print("The dog is", dog_years, "years old.")
elif human_years > 2:
    dog_years = 21 + (human_years - 2) * 4
    print("The dog is", dog_years, "years old.")