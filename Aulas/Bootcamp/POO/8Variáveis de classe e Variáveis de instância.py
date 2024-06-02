# Variáveis de Classe:
# Também conhecidas como atributos de classe.
# São definidas dentro da classe, mas fora de qualquer método.
# São compartilhadas entre todas as instâncias (objetos) da classe.
# Podem ser acessadas diretamente pela classe ou pelas instâncias.
# São úteis para armazenar dados que são comuns a todas as instâncias da classe.


class Estudante:
    escola = "Caic"  # Variável de classe

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno1 = Estudante("Thiago", 1)
aluno2 = Estudante("Isabel", 2)
mostrar_valores(aluno1, aluno2)
aluno1.matricula = 3
mostrar_valores(aluno1, aluno2)
aluno3 = Estudante("Barak", 4)
Estudante.escola = "Stella"
mostrar_valores(aluno1, aluno2, aluno3)

# Variáveis de Instância:
# Também conhecidas como atributos de instância.
# São definidas dentro do método __init__() da classe.
# São específicas para cada instância (objeto) da classe.
# Cada instância tem sua própria cópia das variáveis de instância.
# São acessadas apenas pelas instâncias.


class Pessoa2:
    def __init__(self, nome):
        self.nome = nome  # Variável de instância

    def __str__(self) -> str:
        return f"{self.nome}"


# Criando instâncias da classe Pessoa
p1 = Pessoa2("João")
p2 = Pessoa2("Maria")

# Acessando a variável de instância
print(p1.nome)
print(p2.nome)

# Em resumo, variáveis de classe são compartilhadas entre todas as instâncias de uma classe, enquanto variáveis de instância são específicas para cada instância individual. Elas servem para diferentes propósitos e devem ser escolhidas de acordo com a necessidade específica de cada situação.
