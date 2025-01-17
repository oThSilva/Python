class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor")

    def __str__(self): #Para fazer representação das classe
        return f"{self.__class__.__name__}: {", ".join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"Sim, , estou carregado" if self.carregado else "Não, estou carregado")


moto = Motocicleta("preta", "abc1234", 2)
moto.ligar_motor()

carro =  Carro("Branco","cer8569",4)

caminhao = Caminhao("Roxo", "edf7895", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(moto)
print(carro)
print(caminhao)
