# A conjectura afirma que, não importa qual seja o número inteiro positivo inicial escolhido, a sequência gerada eventualmente alcançará o ciclo 4, 2, 1 e ficará presa nesse ciclo infinitamente.
# A regra é a seguinte:
# Se o número é par, divida por 2.
# Se o número é ímpar, multiplique por 3 e adicione 1.


def collatz(numero):
    while numero > 1:
        if numero % 2 == 0:
            numero //= 2
            print(f"{numero}")
        else:
            numero = numero * 3 + 1
            print(f"{numero}")
    return numero


numero_avaliado = int(input("Digite um numero: "))
numero_para_funcao = collatz(numero_avaliado)
