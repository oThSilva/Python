def somar(num1, num2):
    resultado = num1 + num2
    return resultado


numero1 = int(input("Digite um numero:"))
numero2 = int(input("Digite outro numero:"))

soma = somar(numero1, numero2)
print(f"A soma de {numero1} e {numero2} é {soma}")
