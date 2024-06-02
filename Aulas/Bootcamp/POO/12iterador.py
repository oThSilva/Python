# Iteradores em Python são objetos que permitem que você percorra ou itere sobre uma sequência de elementos, como listas, tuplas, conjuntos ou até mesmo strings. Eles fornecem uma maneira de acessar os elementos de uma coleção de maneira sequencial, sem a necessidade de saber detalhes sobre a implementação subjacente da coleção.

# Acesso sequencial: Iteradores fornecem um método para acessar elementos de uma coleção de maneira sequencial, um por vez.

# Lazy Evaluation: Iteradores geralmente usam uma abordagem de avaliação preguiçosa, o que significa que eles geram elementos conforme necessário, em vez de criar toda a sequência de uma vez.

# Métodos __iter__ e __next__: Um objeto iterador em Python deve implementar os métodos especiais __iter__() e __next__(). O método __iter__() retorna o próprio iterador, enquanto o método __next__() retorna o próximo elemento na sequência ou gera uma exceção StopIteration se não houver mais elementos.

# Iteração em loops: Iteradores podem ser usados em loops for, que automaticamente chamam o método __next__() do iterador para obter os próximos elementos da sequência.


class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except:
            raise StopIteration


for i in MeuIterador(numeros=[1, 2, 3, 4, 5]):
    print(i)

# Exemplo 2:


class MeuIterador2:
    def __init__(self, colecao):
        self.colecao = colecao
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice < len(self.colecao):
            elemento = self.colecao[self.indice]
            self.indice += 1
            return elemento
        else:
            raise StopIteration


# Criando uma lista
lista = [1, 2, 3, 4, 5]

# Criando um iterador para a lista
meu_iterador = MeuIterador2(lista)

# Iterando sobre os elementos da lista usando o iterador
for elemento in meu_iterador:
    print(elemento)
