n1 = int(input("Type your first number: "))
n2 = int(input("Type your first number: "))
n3 = int(input("Type your first number: "))

if n1 == n2 and n1 == n3:
    print("Equal Numbers!")
elif n1 >= n2 >= n3:
    print(n1, n2, n3)
elif n1 >= n3 >= n2:
    print(n1, n3, n2)
elif n2 >= n1 >= n3:
    print(n2, n1, n3)
elif n2 >= n3 >= n1:
    print(n2, n3, n1)
elif n3 >= n1 >= n2:
    print(n3, n1, n2)
elif n3 >= n2 >= n1:
    print(n3, n2, n1)

