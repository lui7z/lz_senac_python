n1 = float(input("Type your first note: "))
n2 = float(input("Type your second note: "))

m = n1 + n2 / 2

if m >= 7:
    print("Approved")
elif m <= 7:
    print("Failed")
elif m == 10:
    print("Approved with Distinction")