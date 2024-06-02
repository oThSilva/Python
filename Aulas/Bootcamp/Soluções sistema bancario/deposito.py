# from funcoesBancarias import extrato


def depositar(valor):

    if valor > 0:

        tipo_movim = "Deposito"
        saldo_atual = 0
        # saldo_atual = extrato.processar_saldo(valor, tipo_movim)
        # += valor_transacao
        # extrato.movimentacoes(valor, tipo_movim)
        # += f"Depósito R$ {valor_transacao:.2f}\n"
        print("Depósito realizado com sucesso")
        print(f"Saldo atual: {saldo_atual:.2f}")
    else:
        print("Digite um valor válido!")

    return
