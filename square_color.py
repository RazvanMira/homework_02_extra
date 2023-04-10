l_one = [1, 2, 3, 4, 5, 6, 7, 8]
l_two = ["a", "b", "c", "d", "e", "f", "g", "h"]
square = input("Introduce the position of the square.\n")
square_list = list(square)
for i in l_one:
    if i == int(square_list[0]):
        for j in range(1, len(l_two)):
            if l_two[j] == square_list[1]:
                if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                    print("The square is black.")
                else:
                    print("The square is white.")