# Encapsulamento é um conceito da programação orientada a objetos que envolve o agrupamento de dados (atributos) e comportamentos (métodos) em uma única unidade chamada de classe. Esse conceito visa ocultar os detalhes internos de uma classe e permitir o acesso controlado aos seus membros.
# Definições:
# Público: Pode ser acessado de fora da classe
# Privado: Não pode ser acessado de fora da classe
# Colocar "_" antes do atributo e da classe para indicar que é uma definição privada
class Conta:
    def __init__(self, nro_agencia, saldo):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
