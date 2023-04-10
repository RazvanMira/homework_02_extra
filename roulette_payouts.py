number = int(input("Introduce a number between 0 or 00 and 36.\n"))
odd_red = [1, 3, 5, 7, 9, 19, 21, 23, 25, 27]
even_red = [12, 14, 16, 18, 30, 32, 34, 36]
odd_black = [11, 13, 15, 17, 29, 31, 33, 35]
even_black = [2, 4, 6, 8, 10, 20, 22, 24, 26, 28]
green = [0, 00]
if number == 0 or number == 00:
    print("Pay 0.")
elif number in range(1, 37):
    print("Pay", number)
if number in odd_red:
    print("Pay red.\nPay odd.")
if number in even_red:
    print("Pay red.\nPay even.")
if number in odd_black:
    print("Pay black.\nPay odd.")
if number in even_black:
    print("Pay black.\nPay even.")
if number > 0 and number <= 18:
    print("Pay 1 to 18.")
if number > 18 and number <= 36:
    print("Pay 19 to 36.")
if number > 36: 
    print("You did not introduce a valid number.")