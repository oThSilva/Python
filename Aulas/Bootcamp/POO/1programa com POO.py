class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): 
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm")
    
    def __del__(self):
        print("Destruindo a instância da classe")

    def __str__(self): #Para fazer representação das classe
        return f"{self.__class__.__name__}: {", ".join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"


caloi = Bicicleta("vermelha", "caloi", 2022, 600)
caloi.buzinar()
caloi.correr()
caloi.parar()

print(caloi.cor, caloi.modelo, caloi.ano, caloi.valor)
# para forçar a destruição da instância
del caloi 
caloi2 = Bicicleta("Verde", "Monark", 2000, 1890)
caloi2.buzinar()  # Mesma coisa = Bicicleta.buzinar(caloi2)
print(caloi2)
