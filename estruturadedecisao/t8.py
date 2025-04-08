n1 = float(input("Type the price of the first product: "))
n2 = float(input("Type the price of the second product: "))
n3 = float(input("Type the price of the third product: "))

if n1 == n2 and n1 == n3:
    print("All prices are equal!")
elif n1 <= n2 and n1 <= n3:
    print("You could buy the product with the", n1, "price!")
elif n2 <= n1 and n2 <= n3:
    print("You could buy the product with the", n2, "price!")
else:
    print("You could buy the product with the", n3, "price!")