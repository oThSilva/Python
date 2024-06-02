# def depositar_dinheiro():
#     print("Depositando dinheiro")

#     def depositando_dolar():
#         print("Depositando Dolares")

#     def depositando_reais():
#         print("Depositando Reais")

#     depositando_dolar()
#     depositando_reais()


# depositar_dinheiro()


# # retornar referencia de funções:
# def pai(numero):
#     def filho_1():
#         print("Sou filho 1")

#     def filho_2():
#         print("Sou filho 2")

#     if numero == 1:
#         return filho_1


# resultado = pai(1)
# resultado()


# # decorators: É uma função que aceita outra função como entrada e retorna uma nova função com algum comportamento adicional.
# def meu_decorator(funcao):
#     def wrapper():
#         print("Antes")
#         funcao()
#         print("Depois")

#     return wrapper


# @meu_decorator
# # Posso aplicar um decorator a uma função usando o símbolo @ seguido do nome do decorator logo acima da definição da função.
# def minha_funcao():
#     print("Executando a função")


# minha_funcao()


# # Desafio

# from datetime import datetime


# def funcao_decorator(funcao):
#     def horario_atual():
#         print(datetime.now())
#         funcao()
#         print(datetime.now())

#     return horario_atual


# @funcao_decorator
# def minha_funcao2():
#     print("Execução da função")


# minha_funcao2()

# # Desafio 2: Crie um decorator chamado verifica_par que envolva uma função e imprima se o resultado da função é par ou ímpar. Aplique o decorator a uma função que retorna um número aleatório.

# import random


# def verifica_par(funcao):
#     def processar():
#         resultado = funcao()
#         print(f"Numero sortido: {resultado}")
#         if resultado % 2 == 0:
#             print(f"O resultado {resultado} é par")
#         else:
#             print(f"O resultado {resultado} é impar")

#     return processar


# @verifica_par
# def numero_aleatorio():
#     return random.randint(1, 10)


# numero_aleatorio()

# Desafio 3: Crie um decorator chamado mede_tempo que imprima o tempo de execução de uma função. Aplique o decorator a uma função que contenha um loop simples.

# import time


# def mede_tempo(funcao):
#     def wrapper():
#         inicio = time.time()
#         funcao()
#         fim = time.time()
#         print(f"A função levou {fim - inicio:.2f} segundos para ser executada.")

#     return wrapper


# @mede_tempo
# def funcao_com_loop():
#     for _ in range(1000000):
#         pass


# funcao_com_loop()
# Desafio 4: Crie um decorator chamado valida_argumento que envolva uma função que recebe dois argumentos e imprima se esses argumentos são inteiros. Aplique o decorator a uma função que realiza uma operação matemática.


def valida_argumento(funcao):
    def wrapper(arg1, arg2):
        if isinstance(arg1, int) and isinstance(arg2, int):
            funcao(arg1, arg2)
        else:
            print("Os argumentos precisam ser inteiros.")

    return wrapper


@valida_argumento
def soma(a, b):
    resultado = a + b
    print(f"A soma de {a} e {b} é {resultado}.")


soma(10, 10)
