class Pessoa:
    def __init__(self):
        self.nome = str(input("Digite o Nome da Pessoa: "))
        self.idade = int(input(f"Digite a Idade de {self.nome}: "))
        self.peso = float(input(f"Digite o Peso de {self.nome}: "))
        self.altura = float(input(f"Digite a Altura de {self.nome}: "))
        self.opcao = None

        self.idadeog = self.idade
        self.pesoog = self.peso
        self.alturaog = self.altura

    def envelhecer(self):
        self.anos = int(input(f"Digite Quantos Anos {self.nome} Envelheceu: "))
        self.idade += self.anos
        if self.idadeog < 21:
            if self.idade <21:
                crescimento = self.anos * 0.05
            else:
                crescimento = (21 - self.idadeog) * 0.05
            self.crescer(crescimento)

        print(f"                                       Após Envelhecer sua nova Idade é: {self.idade} e sua altura é: {self.altura}")

    def engordar(self):
        self.gordura = float(input("Digite o Ganho de Peso: "))
        self.peso += self.gordura
        print(f"                                       Após Engordar seu novo Peso é: {self.peso}")

    def emagrecer(self):
        self.perda = float(input("Digite a Perda de Peso: "))
        if self.peso < self.perda:
            self.emagrecer()
        else:
            self.peso -= self.perda
        print(f"                                       Após Emagrecer seu novo Peso é: {self.peso}")

    def crescer(self, ganho):
        self.altura += ganho
        print(f"                                       Após Crescer sua nova Altura é: {self.altura}")

    def __str__(self):
        if self.opcao is None:
            self.op()
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        return (f"As Informações Originais da Pessoa são:\nNome = {self.nome}\nSua Idade é = {self.idadeog}\nSeu Peso é = {self.pesoog}\nE sua Altura é = {self.alturaog}")

    def op(self):
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        self.opcao = str(input(f"                                       Digite uma das Opções desejadas:\nEnvelhecer - 1                   Engordar - 2                    Emagrecer - 3                   Crescer - 4\n"))
        if self.opcao == "1":
            self.envelhecer()
        elif self.opcao == "2":
            self.engordar()
        elif self.opcao == "3":
            self.emagrecer()
        elif self.opcao == "4":
            self.crescer(float(input("Digite o Ganho de Altura: ")))

Fulano1 = Pessoa()
print(Fulano1)