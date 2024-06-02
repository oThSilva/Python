# Principios de Clean Code
# 1 - Dê nomes significativos para as coias
# 2 - Funções pequenas que resolva uma coisa
# 3 - Quanto menos parâmetros na função melhor
# 4 - Uso funções para organizar o código e economizar linhas( principio DRY)

# Módulo 3 - Projeto 2 - solução do professor
# from turtle import Turtle

# t = Turtle()
# t.speed(1)


# def obeter_distancia():
#     resposta = int(input("Quantos pixels devemos movimentar para a frente? "))
#     return resposta


# def rotacionar_turtle(t):
#     movimentar_para_lado = input(
#         "Rotacionar para d:direta, e:esquerda n:não rotacionar "
#     )
#     if movimentar_para_lado == "d":
#         rotacionar_para_direita(t)
#     elif movimentar_para_lado == "e":
#         rotacionar_para_esquerda(t)


# def rotacionar_para_direita(t):
#     angulo = int(input("Quanto para a direta devemos rotacionar? "))
#     t.right(angulo)


# def rotacionar_para_esquerda(t):
#     angulo = int(input("Quanto para a esquerda devemos rotacionar? "))
#     t.left(angulo)


# while True:
#     direcao = input('Para qual direção devemos ir? "f:frente" ou "t:trás" ')
#     if direcao == "f":
#         distancia = obeter_distancia()
#         rotacionar_turtle(t)
#         t.forward(distancia)
#     if direcao == "t":
#         distancia = obeter_distancia()
#         rotacionar_turtle(t)
#         t.backward(distancia)
#     resposta = input("Continuar andando?")
#     if resposta not in ("sim", "s"):
#         break
# ============================================================================

# Módulo 3 - projeto2 - solução 1

from turtle import Turtle

tartaruga = Turtle()
tartaruga.speed(1)


def obter_distancia():
    distancia = int(input("Quantos pixels devem ser percorridos?"))
    return distancia


def rotacionar_turtle(tartaruga):
    direta_esquerda = input("Rotacionar para d:direita e:esquerda n:não rotacionar")
    if direta_esquerda == "d":
        rotacionar_para_direita(tartaruga)
    elif direta_esquerda == "e":
        rotacionar_para_esquerda(tartaruga)


def rotacionar_para_direita(tartaruga):
    angulo = int(input("Quantos pixels devem ser percorridos para direita?"))
    tartaruga.right(angulo)


def rotacionar_para_esquerda(tartaruga):
    angulo = int(input("Quantos pixels devem ser percorridos para esquerda?"))
    tartaruga.left(angulo)


while True:
    frente_tras = input("Para qual direção devemos ir? 'f:frente ou 't:trás: ")
    if frente_tras == "f":
        distancia = obter_distancia()
        rotacionar_turtle(tartaruga)
        tartaruga.forward(distancia)

    elif frente_tras == "t":
        distancia = obter_distancia()
        rotacionar_turtle(tartaruga)
        tartaruga.backward(distancia)
    resposta = input("Continuar andando?")
    if resposta not in ("sim", "s"):
        break

input()
