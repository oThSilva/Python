# Uma classe abstrata em programação orientada a objetos é uma classe que não pode ser instanciada diretamente, mas é projetada para ser usada como uma classe base para outras classes. Ela geralmente contém métodos abstratos, que são métodos sem implementação, destinados a serem sobrescritos por subclasses concretas.
# Não pode ser instanciada diretamente: Uma classe abstrata não pode ser usada para criar objetos diretamente. Ela é projetada para ser uma classe base para outras classes.
# Métodos abstratos: Uma classe abstrata pode conter métodos abstratos, que são definidos sem uma implementação. Esses métodos devem ser implementados por classes filhas.
# Define um contrato: Uma classe abstrata define um contrato que outras classes devem cumprir, garantindo que elas forneçam implementações para todos os métodos abstratos definidos pela classe abstrata.
# Promove a reutilização de código: Classes abstratas são úteis para compartilhar comportamentos comuns entre várias subclasses e promover a reutilização de código.
# Em Python, classes abstratas são definidas usando o módulo abc e o decorador @abstractmethod para indicar métodos abstratos.
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass


class Cao(Animal):
    def fazer_som(self):
        print("Au Au!")


class Gato(Animal):
    def fazer_som(self):
        print("Miau!")


# Neste exemplo, Animal é uma classe abstrata que define um método abstrato fazer_som(). As classes Cao e Gato são subclasses de Animal e fornecem implementações concretas para o método fazer_som(). Assim, Animal define um contrato que outras classes devem cumprir, garantindo que todas as subclasses forneçam uma implementação para o método fazer_som().
