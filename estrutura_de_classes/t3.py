class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.opcao = None

    def opcao(self):
        self.opcao = str(input(f"Digite uma das Opções desejadas:\nEnvelhecer - 1\nEngordar - 2\nEmagrecer - 3\nCrescer - 4"))

    def __str__(self):
        if self.opcao is None:
            self.opcao()
        return (f"A Pessoa tem o Nome = {self.nome}\nSua Idade é = {self.idade}\nSeu Peso é = {self.peso}\nE sua Altura é = {self.altura}")

fulano = Pessoa("Luiz", 19, 70, 1.70)
print(fulano)