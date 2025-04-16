class Quadrado:
    def __init__(self):
        self.lado = float(input("Type the side of your Square: "))

        self.area = None

    def calcular(self):
        self.area = self.lado * self.lado
        return self.area

    def __str__(self):
        if self.area is None:
            self.calcular()
        return (f"The side of your square is equal to: \033[31m{self.lado}\033[0m\nAnd the Area is equal to = \033[32m{self.area}\033[0m")

quadradoredondo = Quadrado()
print(quadradoredondo)
