n1 = int(input("Type your first number: "))
n2 = int(input("Type your second number: "))

if n1 > n2:
    print("The number", n1, "is bigger than:", n2)
elif n2 > n1:
    print("The number", n2, "is bigger than:", n1)
elif n1 == n2:
    print("The number", n1, "and", n2, "are equals!")