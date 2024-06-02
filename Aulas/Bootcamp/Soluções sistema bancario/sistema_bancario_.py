# Criar um sistema bancario com as operações: sacar, depositar, e visualizar extrato.

# Deposito:
# Depositar somente valores positivos
# Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato

# Saque:
# Só é permitido 3 saques diários com limite máximo de R$ 500,00 por saque
# caso o saldo seja insufciente, informar o usuario
# Todos os saques devem ser armazenados em uma variável e exibidos na operação extrato

# Extrato:
# Deve listar todos os depósitos e saques realizados na conta
# No fim da lista deve ser exibido o saldo atual da conta
# Os valores devem ser exibidos utilizando o formato R$ 1500,45

# ----------------------------------------------------------------------------#
# 01 refatoração  do sistema bancario
# Objetivo geral: Transformar saque, depósito e extrato em funções.

# Extrato: Argumentos posicionais (saldo) e nomeados (extrato)

# Saque: Argumentos nomeados (sugestões: saldo, valor, extrato, limite, numero_saque, limite_saque), Sugestões de retorno: saldo e extrato

# Deposito: Argumentos posicionais (sugestões: saldo, valor, extrato), Sugestões de retorno: saldo e extrato

# Criar Três novas funções:
# Cadastrar usuário (clente): O programa deve armazenar os usuarios em uma lista. Usuario: Nome, Data de nascimento, CPF(somente numeros, não pode cadastrar mais de um usuario por CPF) e endereço(é uma string com formato: Logradouro, Bairro, Cidade/sigla estado

# Cadastrar conta bancaria (vincular com usuario): O programa deve armazenar contas em uma lista. Conta: Agencia(0001), numero da conta(O numero da conta é sequencial, iniciado em 1) e usuario. o usario pode ter mais de uma conta, mas uma conta pertence a somente um usuario e cada conta tem que ser vinculada a um usuario.
# Para vincular um usuario a uma conta, filtre a lista de usuarios buscando o numero do CPF informado para cada usuario da lista

# Listar contas



menu = """
[1] - Depositar 
[2] - Sacar
[3] - Extrato
[4] - Cadastrar Usuário
[5] - Cadastrar Conta Bancária
[6] - Listar Contas
[0] - Sair 
"""
saldo_conta = 0
limite = 500
extrato_transacoes = ""
numero_saques = 0
LIMITE_SAQUE = 3
cliente = ""


def depositar(valor, saldo_conta, extrato_transacoes):
    if valor > 0:
        extrato_transacoes += f"Depósito R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso")
        saldo_conta += valor
        print(f"Saldo atual: {saldo_conta:.2f}")
        extrato_transacoes += f"Depósito R$ {valor:.2f}\n"

    return saldo_conta, extrato_transacoes


def extrato(saldo_conta, *, extrato_transacoes):

    print("\n-----------------------Extrato-----------------------")
    print(
        "Não foram realizadas movimentações."
        if not extrato_transacoes
        else extrato_transacoes
    )
    print(f"\n Saldo: R$ {saldo_conta:.2f}")
    print("-------------------------------------------------------")

    return extrato_transacoes


def sacar(*, valor, saldo_conta, numero_saques, extrato_transacoes):

    limite = 500
    LIMITE_SAQUE = 3

    if valor > saldo_conta:
        print("Saldo insuficiente")
    elif valor > limite:
        print(f"O limite é de R$ {limite} por saque")
    elif numero_saques >= LIMITE_SAQUE:
        print("O limite de saques diario é de 3 saques")
    elif valor > 0:
        saldo_conta -= valor
        extrato_transacoes += f"Saque R$ {valor:.2f}\n"
        print(f"Saldo atual: {saldo_conta:.2f}")
        numero_saques += 1
    else:
        print("Digite um valor válido")

    return saldo_conta, numero_saques, extrato_transacoes

    # def cadastrar_usuario(a):
    cliente = {
        "Nome": {},
        "Data de nascimento": {},
        "CPF": {},
    }

    endereco = {
        "logradouro": {},
        "Bairro": {},
        "Cidade": {},
        "sigla estado": {},
    }
    usuario = []
    print("Cadastro de Usuario")
    for i in cliente.keys():
        b = input(f"{i}: ")
        cliente[i] = b
    for j in endereco.keys():
        c = input(f"insira os dados de endereço{j}: ")
        endereco[j] = c
        # cliente["endereco"] = endereco.items()

    print(cliente, endereco)

    usuario = [cliente, endereco]
    print(usuario)
    # cloenteNovo = tuple(cliente.items())
    # print(
    #     f"""
    #     Usuario cadastrado:
    #     Nome: {cloenteNovo[0][1]}
    #     """
    # )
    # INSIRA OS DADOS DO USUARIO
    # FOR {
    # PRINT 0: ___
    # print 1:

    #     dados do usuario completos return
    # }

    # usuario cadastrado:
    #     Nome: nome_cliente

    # for i, item in cliente.keys(), cliente.items():
    #     cliente = input(f"{i}: {item}")
    #     print("nome da variavel " + i, " ", "nome do item" + item)
    # endereco = {
    #     "logradouro": {rua},
    #     "Bairro": {bairro},
    #     "Cidade": {cidade},
    #     "sigla estado": {estado},
    # }

    return cliente

while True:

    opcao = int(input(menu))
    if opcao == 1:
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            tupla_deposito = depositar(valor, saldo_conta, extrato_transacoes)
            saldo_conta = tupla_deposito[0]
            extrato_transacoes = tupla_deposito[1]
        else:
            print("Digite um valor válido!")
    elif opcao == 2:
        valor = float(input("Digite o valor do saque: "))
        tupla_saque = sacar(
            valor=valor,
            saldo_conta=saldo_conta,
            numero_saques=numero_saques,
            extrato_transacoes=extrato_transacoes,
        )
        saldo_conta = tupla_saque[0]
        numero_saques = tupla_saque[1]
        extrato_transacoes = tupla_saque[2]
    elif opcao == 3:
        extrato_transacoes = extrato(saldo_conta, extrato_transacoes=extrato_transacoes)

    elif opcao == 0:
        break
    else:
        print("Operação inválida!")

# usuario = ""
# usuario = ["isabel", ""
           
def add_usuario(*, usuario=usuario, endereco):
    # Usuario: Nome, Data de nascimento, CPF(somente numeros, não pode cadastrar mais de um usuario por CPF)
    # e endereço(é uma string com formato: Logradouro, Bairro, Cidade/sigla estado
    
    
    
    endereco = ["lote", "bairro", "cidade", "estado_sigla[2]"]
    usuario = ["Nome", "data_nasc", "cpf", "endereco[" "]"]
    if usuario[2] > num
    print("Digite um cpf valido: " + usuario[2])
    elif usuario[2] == usuario[2]
    
    return cliente


# menu = """
# [1] - Depositar
# [2] - Sacar
# [3] - Extrato
# [0] - Sair
# """
# saldo_conta = 0
# limite = 500
# extrato_transacoes = ""
# numero_saques = 0
# LIMITE_SAQUE = 3

# while True:

#     opcao = int(input(menu))
#     if opcao == 1:
#         valor = float(input("Digite o valor do depósito: "))

#         if valor > 0:
#             saldo_conta += valor
#             extrato_transacoes += f"Depósito R$ {valor:.2f}\n"
#             print("Depósito realizado com sucesso")
#             print(f"Saldo atual: {saldo_conta:.2f}")
#         else:
#             print("Digite um valor válido!")

#     elif opcao == 2:
#         valor = float(input("Digite o valor do saque: "))
#         if valor > saldo_conta:
#             print("Saldo insuficiente")
#         elif valor > limite:
#             print(f"O limite é de R$ {limite} por saque")
#         elif numero_saques >= LIMITE_SAQUE:
#             print("O limite de saques diario é de 3 saques")
#         elif valor > 0:
#             saldo_conta -= valor
#             extrato_transacoes += f"Saque R$ {valor:.2f}\n"
#             print("Saque realizado com sucesso")
#             print(f"Saldo atual: {saldo_conta:.2f}")
#             numero_saques += 1
#         else:
#             print("Digite um valor válido")

#     elif opcao == 3:
#         print("\n-----------------------Extrato-----------------------")
#         print(
#             "Não foram realizadas movimentações."
#             if not extrato_transacoes
#             else extrato_transacoes
#         )
#         print(f"\n Saldo: R$ {saldo_conta:.2f}")
#         print("-------------------------------------------------------")

#     elif opcao == 0:
#         break
#     else:
#         print("Operação inválida!")
