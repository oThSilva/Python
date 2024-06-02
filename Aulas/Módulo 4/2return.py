# return é uma instrução usada em funções para especificar o valor que a função deve retornar quando é chamada. Essencialmente, é a maneira pela qual uma função pode fornecer um resultado de volta para o código que a chamou.


# função que processa dados:
print("Ola")


def exibir_cotacao_do_dia(moeda):
    if moeda == "usd":
        print(5.47)


exibir_cotacao_do_dia("usd")

# função que retorna dados:
cidade = input("Qual é a cidade?")


def obter_cotacao_do_dia(moeda):
    if moeda == "usd":
        return 5.47


cotacao = obter_cotacao_do_dia("usd")
if cotacao > 5:
    print("Investir na bolsa americana")
else:
    print("Não investir")


# Múltiplos Valores de Retorno: Uma função pode retornar múltiplos valores separados por vírgula.
def divide_e_resto(dividendo, divisor):
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto


resultado_divisao, resto_divisao = divide_e_resto(10, 2)
print(resultado_divisao, resto_divisao)
