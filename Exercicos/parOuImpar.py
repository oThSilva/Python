def par_ou_impar(numero):
    while numero > 0:
        if numero % 2 == 0:
            print(f"{numero} PAR")
            numero -= 1
        else:
            print(f"{numero} ÍMPAR")
            numero -= 1

    print("Fim do loop")

    return numero


numero_verificado = int(input("Digite um numero: "))
verificar = par_ou_impar(numero_verificado)
