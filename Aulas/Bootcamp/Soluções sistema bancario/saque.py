def sacar(valor):

    limite = 500
    numero_saques = 0
    LIMITE_SAQUE = 3
    saldo = 0
    extrato = "1"
    # saldo, valor, extrato, limite, numero_saques, limite_saque
    if valor > saldo:
        print("Saldo insuficiente")
    elif valor > limite:
        print(f"O limite é de R$ {limite} por saque")
    elif numero_saques >= LIMITE_SAQUE:
        print("O limite de saques diario é de 3 saques")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque R$ {valor:.2f}\n"
        print(f"Saldo atual: {saldo:.2f}")
        numero_saques += 1
    else:
        print("Digite um valor válido")

    return saldo, extrato
