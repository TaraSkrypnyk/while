from math import*
try:
    p = int(input("Введіть сторону квадрата "))
    x = y = p
    i = 0
    j = 0
    while i < x:
        j = 0
        while j < y:
            if ((i + j) < (floor(p/2))):
                print("     ", end="")
            elif ((i + j) > (p+(floor(p/2)))):
                print("     ", end="")
            elif ((i + j) >= (p+(floor(p/2)))):
                print("     ", end="")
            elif ((i - j) > (floor(p/2))):
                print("     ", end="")
            elif ((j - i) > (floor(p/2))):
                print("     ", end="")
            else:
                print("[" + str(i) + " " + str(j) + "]", end="")
            j += 1
        print()
        i += 1
except Exception as e:
    print (e)