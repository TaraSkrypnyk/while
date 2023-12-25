try:
    p = int(input("Введіть сторону квадрата "))
    x = y = p
    def top():
        i = 0
        j = 0
        while i < x:
            j = 0
            while j < y:
                if ((i + j) <= (p - 1)) and (i <= j):
                    print("* ", end="")
                else:
                    print("  ", end="")
                j += 1
            print()
            i += 1
    def right():




except Exception as e:
    print (e)