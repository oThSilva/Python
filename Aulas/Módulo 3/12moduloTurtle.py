from turtle import Turtle
#Inicializar uma turtle
t = Turtle()
#Definir a velocidade
t.speed(1)
#Movimentar a turtle para frente
t.forward(100)
#Rotacionar em X graus para a direita 
t.right(90)
t.forward(100)
#Rotacionar em X graus para a esquerda 
t.left(90)
t.forward(100)
#movimentar a turtle para trás 
t.backward(200)
input()

# t = Turtle()
# t.speed(1)
# while True:
#     distancia = int(input('Distância a percorrer?'))
#     t.forward(distancia)