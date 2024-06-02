def consulta_extrato(saldo, extrato):
    saldo = 10000
    extrato = ""
    print("\n-----------------------Extrato-----------------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("-------------------------------------------------------")

    return saldo, extrato


def processar_saldo(valor, tipo_movim):
    saldo = 0
    if tipo_movim == "Deposito":
        # adionar saldo
        print("opção Deposito")
        saldo += valor
    elif tipo_movim == "Saque":
        # subtrair saldo
        print("opção Saque")
        saldo -= valor
    elif tipo_movim == "consulta":
        # print(f"\n Saldo: R$ {saldo:.2f}")
        return saldo
    else:
        print("opção inválida")
    return saldo


def movimentacoes(valor, tipo_movim):
    # incluir movimentação
    extrato = ""
    # tipo_movim = "consulta"

    if tipo_movim == "Deposito":
        extrato += f"Depósito R$ {valor:.2f}\n"
    elif tipo_movim == "Saque":
        extrato += f"Saque R$ {valor:.2f}\n"
    elif tipo_movim == "consulta":
        tipo_movim = "consulta"
        saldo = processar_saldo(valor, tipo_movim)

    print("\n-----------------------Extrato-----------------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("-------------------------------------------------------")

    return extrato
