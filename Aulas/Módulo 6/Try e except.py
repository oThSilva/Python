# Try e except são palavras chaves para lidar com exeções(erros) que podem ocorrer durante a execução de um código.

try:
    valor = int(input("Digite o valor: "))
    print(valor * 5.25)
except:
    print("Favor, digite somente numeros")

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print("O resultado é:", resultado)
except ZeroDivisionError as erro:
    print("Erro: Divisão por zero não é permitida.")
except ValueError as erro:
    print("Erro: Valor inválido. Por favor, digite um número inteiro.")
