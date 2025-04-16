# Cafetéria do seu Kleberson
opcao = 0
menu = ['1', '2', '3', '4', '5', '6', '7', '8']

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cardapio():
    print("""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            Bem Vindo a Cafetéria do seu Kleberson!
            Dê uma olhada no Nosso Cardápio
    
            1 - Café
            2 - Cappuccino
            3 - Torta
            4 - Bolo
            5 - Bolacha
            6 - Pão
            7 - Croissant
            8 - Folheado
    -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")

def pagamento():
    if opcao in menu:
        clear()
        print("O Seu pedido ficou no valor de 500 pesos mexicanos.")

while True:
    cardapio()
    opcao = str(input("Por Favor digite o Número referente a opção escolhida: ")).strip()
    if opcao not in menu:
        opcao = 0
        print("\033[31mPor Favor Digite uma das Opções do Menu!\033[0m")
    else:
        clear()
        print("\033[32mPedido Confirmado\033[0m")
        opcao2 = str(input("""
        Deseja mais Algo?
        S - Sim, N - Não (Prosseguir para o Pagamento)\n""")).strip().upper()

        if opcao2 == "S":
            cardapio()
        elif opcao2 == "N":
            pagamento()
            break
        else:
            print("\033[31mOpção inválida! Digite 'S' para Sim ou 'N' para Não.\033[0m")
