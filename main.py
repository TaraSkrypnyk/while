try:
    p = int(input("Введіть сторону квадрата "))
    x = y = p
    i = 0
    j = 0
    while i < x:
        j = 0
        while j < y:
            if ((i + j) >= (p - 1)):
                print("* ", end="")
            else:
                print("  ", end="")
            j += 1
        print()
        i += 1
except Exception as e:
    print (e)