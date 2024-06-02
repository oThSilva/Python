# Uma interface especifica um contrato que uma classe deve cumprir, garantindo que ela tenha certos comportamentos.
# Contrato de Métodos: Uma interface define um conjunto de métodos que uma classe deve fornecer. Esses métodos são apenas assinaturas, sem implementação.
# Implementação na Classe: Qualquer classe que implemente uma interface deve fornecer implementações para todos os métodos definidos pela interface.
# Polimorfismo: Interfaces permitem que diferentes classes tenham comportamentos comuns, facilitando a substituição de objetos em código.
# Interfaces são úteis para garantir que várias classes tenham um conjunto comum de comportamentos, sem se preocupar com a implementação específica de cada classe. Por exemplo, considere uma interface Animal com os métodos fazer_som() e mover(). Qualquer classe que represente um animal deve implementar esses métodos:
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class Cao(Animal):
    def fazer_som(self):
        print("Au Au!")

    def mover(self):
        print("Correndo")


class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

    def mover(self):
        print("Saltando")
