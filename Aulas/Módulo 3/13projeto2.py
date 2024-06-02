# solução 1

# from turtle import Turtle

# tartaruga = Turtle()
# tartaruga.speed(1)

# while True:
#     frente_tras = input("Para qual direção devemos ir? 'f:frente ou 't:trás: ")
#     if frente_tras == "f":
#         distancia = int(input("Quantos pixels devem ser percorridos para frente?"))

#         direta_esquerda = input("Rotacionar para d:direita e:esquerda n:não rotacionar")

#         if direta_esquerda == "d":
#             angulo = int(input("Quantos pixels devem ser percorridos para direita?"))
#             tartaruga.right(angulo)

#         elif direta_esquerda == "e":
#             angulo = int(input("Quantos pixels devem ser percorridos para esquerda?"))
#             tartaruga.left(angulo)
#         tartaruga.forward(distancia)

#     elif frente_tras == "t":
#         distancia = int(input("Quantos pixels devem ser percorridos para trás?"))

#         direta_esquerda = input("Rotacionar para d:direita e:esquerda n:não rotacionar")

#         if direta_esquerda == "d":
#             angulo = int(input("Quantos pixels devem ser percorridos para direita?"))
#             tartaruga.right(angulo)
#         elif direta_esquerda == "e":
#             angulo = int(input("Quantos pixels devem ser percorridos para esquerda?"))
#             tartaruga.left(angulo)
#         tartaruga.backward(distancia)
#     resposta = input("Continuar andando?")
#     if resposta not in ("sim", "s"):
#         break

# input()

###########################################################

# solução 1 (refatorada)
# from turtle import Turtle


# def mover_tartaruga(tartaruga, direcao, distancia):
#     if direcao == "f":
#         tartaruga.forward(distancia)
#     elif direcao == "t":
#         tartaruga.backward(distancia)


# def rotacionar_tartaruga(tartaruga, direcao, angulo):
#     if direcao == "d":
#         tartaruga.right(angulo)
#     elif direcao == "e":
#         tartaruga.left(angulo)


# def main():
#     tartaruga = Turtle()
#     tartaruga.speed(1)
#     distancia = 0
#     continuando = True

#     while continuando:
#         frente_tras = input("Para qual direção devemos ir? 'f:frente ou 't:trás: ")
#         distancia = int(input(f"Quantos pixels devem ser percorridos? "))

#         direcao_rotacao = input(
#             "Rotacionar para d:direita e:esquerda n:não rotacionar: "
#         )
#         if direcao_rotacao != "n":
#             angulo = int(input("Quantos graus devem ser rotacionados? "))
#             rotacionar_tartaruga(tartaruga, direcao_rotacao, angulo)

#         mover_tartaruga(tartaruga, frente_tras, distancia)

#         continuar = input("Continuar andando? s:sim n:não: ")
#         continuando = continuar == "s"

#     input()


# if __name__ == "__main__":
#     main()

###########################################################

# solução do professor:

# from turtle import Turtle

# t = Turtle()
# t.speed(1)
# while True:
#     direcao = input('Para qual direção devemos ir? "f:frente" ou "t:trás" ')
#     if direcao == "f":
#         distancia = int(input("Quantos pixels devemos movimentar para a frente? "))
#         movimentar_para_lado = input(
#             "Rotacionar para d:direta, e:esquerda n:não rotacionar "
#         )
#         if movimentar_para_lado == "d":
#             angulo = int(input("Quanto para a direta devemos rotacionar? "))
#             t.right(angulo)
#         elif movimentar_para_lado == "e":
#             angulo = int(input("Quanto para a esquerda devemos rotacionar? "))
#             t.left(angulo)
#         t.forward(distancia)
#     if direcao == "t":
#         distancia = int(input("Quantos pixels devemos movimentar para a trás? "))
#         movimentar_para_lado = input(
#             "Rotacionar para d:direta, e:esquerda n:não rotacionar "
#         )
#         if movimentar_para_lado == "d":
#             angulo = int(input("Quanto para a direta devemos rotacionar? "))
#             t.right(angulo)
#         elif movimentar_para_lado == "e":
#             angulo = int(input("Quanto para a esquerda devemos rotacionar? "))
#             t.left(angulo)
#         t.backward(distancia)
#     resposta = input("Continuar andando?")
#     if resposta not in ("sim", "s"):
# break
###########################################################

# solução do professor(refatorada):
from turtle import Turtle


def movimentar_tartaruga(t, direcao, distancia):
    if direcao == "f":
        movimentar_para_lado = input(
            "Rotacionar para d:direita, e:esquerda n:não rotacionar "
        )
        if movimentar_para_lado == "d":
            angulo = int(input("Quanto para a direita devemos rotacionar? "))
            t.right(angulo)
        elif movimentar_para_lado == "e":
            angulo = int(input("Quanto para a esquerda devemos rotacionar? "))
            t.left(angulo)
        t.forward(distancia)
    elif direcao == "t":
        movimentar_para_lado = input(
            "Rotacionar para d:direita, e:esquerda n:não rotacionar "
        )
        if movimentar_para_lado == "d":
            angulo = int(input("Quanto para a direita devemos rotacionar? "))
            t.right(angulo)
        elif movimentar_para_lado == "e":
            angulo = int(input("Quanto para a esquerda devemos rotacionar? "))
            t.left(angulo)
        t.backward(distancia)


def main():
    t = Turtle()
    t.speed(1)

    while True:
        direcao = input('Para qual direção devemos ir? "f:frente" ou "t:trás" ')
        distancia = int(input(f"Quantos pixels devemos movimentar? "))

        movimentar_tartaruga(t, direcao, distancia)

        resposta = input("Continuar andando? (sim/s): ")
        if resposta.lower() not in ("sim", "s"):
            break


if __name__ == "__main__":
    main()
