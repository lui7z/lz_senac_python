n = int(input("Type your number: "))

def jose(x):
    y = x % 2
    if y == 0:
        print("P")
    elif y == 1:
        print("N")

jose(n)