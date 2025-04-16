class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def __str__(self):
        return (f"A sua Bola tem a Cor = {self.cor}\nSua Circunferência é = {self.circunferencia}\nE seu material = {self.material}")

bolaquadrada = Bola("Azul", 10, "Metal")
print(bolaquadrada)
