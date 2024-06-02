def calcular_soma_de_intervalo(inico, fim):
    soma = 0
    for numero in range(inico, fim + 1):
        soma += numero
        print(numero, soma)
    return soma


inicio_de_intervalo = int(input("Digite o inicio: "))
fim_de_intervalo = int(input("Digite o fim: "))

resultado = calcular_soma_de_intervalo(inicio_de_intervalo, fim_de_intervalo)
print(
    f"A soma do intervalo de {inicio_de_intervalo} a {fim_de_intervalo} é: {resultado}"
)
