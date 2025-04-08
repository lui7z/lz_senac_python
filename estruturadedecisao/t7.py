n1 = float(input("Type a number: "))
n2 = float(input("Type a number: "))
n3 = float(input("Type a number: "))

if n1 == n2 and n1 == n3:
    print("The numbers are equal!")
elif n1 >= n2 and n1 >= n3:
    print(n1, "is the biggest Number!")
elif n2 >= n1 and n2 >= n3:
    print(n2, "is the biggest Number!")
elif n3 >= n1 and n3 >= n2:
    print(n3, "is the biggest Number!")

if n1 <= n2 and n1 <= n3:
    print(n1, "is the minor Number!")
elif n2 <= n1 and n2 <= n3:
    print(n2, "is the minor Number!")
else:
    print(n3, "is the minor Number!")