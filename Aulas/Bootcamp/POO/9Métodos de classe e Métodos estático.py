# Métodos de Classe:
# São métodos que operam na classe em si, em vez de em instâncias individuais da classe.
# São definidos usando o decorador @classmethod.
# O primeiro parâmetro de um método de classe é convencionalmente chamado de cls, que se refere à classe em si.
# Podem acessar e modificar variáveis de classe.
# São comumente usados para criar construtores alternativos, métodos de fábrica ou métodos que trabalham com variáveis de classe


class Pessoa:
    quantidade = 0  # Variável de classe

    def __init__(self, nome):
        self.nome = nome
        Pessoa.quantidade += 1

    @classmethod
    def total_pessoas(cls):
        return cls.quantidade


# Criando instâncias da classe Pessoa
p1 = Pessoa("João")
p2 = Pessoa("Maria")

# Chamando o método de classe
print(f"Total de pessoas {Pessoa.total_pessoas()}")  # Saída: 2


# Métodos Estáticos:
# São métodos que não operam em instâncias ou em classes, mas são logicamente relacionados à classe.
# São definidos usando o decorador @staticmethod.
# Não recebem automaticamente uma referência para a instância ou para a classe.
# Podem ser chamados tanto pela classe quanto pelas instâncias, mas não têm acesso a variáveis de instância ou de classe.
# São úteis para funções que não precisam de acesso a variáveis de instância ou de classe, mas estão logicamente relacionadas à classe.


class Matematica:
    @staticmethod
    def soma(x, y):
        return x + y


# Chamando o método estático
print(f"O resultado da soma é s{Matematica.soma(3, 5)}")  # Saída: 8
