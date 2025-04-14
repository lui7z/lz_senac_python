n = int(input("Type your number: "))

def jose(number):
    for i in range(1, number + 1):
        linha = (str(i) + " ") * i
        print(linha.strip())

jose(n)