# Em Python, a função dir() é uma função integrada que retorna uma lista de nomes de atributos de um objeto. Esses atributos podem ser métodos, atributos de dados, ou outros objetos aninhados dentro do objeto original. A função dir() é útil para explorar a estrutura e os atributos de um objeto em Python, especialmente quando você está trabalhando com bibliotecas ou módulos desconhecidos.
# Sintaxe:


class Exemplo:
    def __init__(self):
        self.valor = 10

    def metodo(self):
        pass


objeto = Exemplo()

atributos = dir(objeto)
print(atributos)
