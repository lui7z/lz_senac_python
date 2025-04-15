n = int(input("Type your number: "))

def jose(number):
    for i in range(1, number + 1):
        linha = " ".join(str(x) for x in range(1, i + 1))
        print(linha)

jose(n)