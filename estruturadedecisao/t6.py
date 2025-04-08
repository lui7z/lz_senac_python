n1 = float(input("Type a number: "))
n2 = float(input("Type a number: "))
n3 = float(input("Type a number: "))

if n1 > n2 and n1 > n3:
    print(n1, "is the biggest Number!")
elif n2 > n1 and n2 > n3:
    print(n2, "is the biggest Number!")
elif n3> n1 and n3> n2:
    print(n3, "is the biggest Number!")
elif n1 and n2 > n3:
    print(n1, "and", n2, "are the biggest Numbers!")
elif n2 and n3 > n1:
    print(n2, "and", n3, "are the biggest Numbers!")
elif n1 and n3 > n2:
    print(n1, "and", n2, "are the biggest Numbers!")
else:
    print("The numbers are equal!")

def maior(x, y, z):
    if x == y and x == z:
        return x
    elif x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

