def boas_vindas():
    print("Bem vindo!")


boas_vindas()

# função com parametro


def boas_vindas_personalizada(nome):
    print(f"Bem vindo {nome}")


boas_vindas_personalizada("Th")


# valor padrão
# argumentos com valores definidos, devem ficar por ultimo
def apresentar_lugar(
    horario_de_funcionamento,
    lugar="Minha casa",
):
    print(f"Conheça {lugar}, horário de funcionamento {horario_de_funcionamento}")


apresentar_lugar("08:00 as 18:00", "Padaria do Th")


def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado de {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)

operacao = somar
print(operacao(5, 5))


# desafio 1
# nome = ""
# sobrenome = ""


# def gerar_nome_completo(nome, sobrenome):
#     nome = input("Nome: ")
#     sobrenome = input("Sobrenome:")
#     print(f"Bem vindo {nome} {sobrenome}")


# gerar_nome_completo(nome, sobrenome)

# desafio 2


def calcular_valores():
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    preco_total = preco * quantidade
    print(f"Preço total: R${preco_total}")


calcular_valores()
