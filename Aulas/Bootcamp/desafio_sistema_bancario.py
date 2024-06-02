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

# ----------------------------------------------------------------------------#

# 02 refatoração do sistema bancario
# Objetivo geral: atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários.

# Refatoração 01

# def depositar(valor_deposito, saldo, extrato):
#     if valor_deposito > 0:
#         saldo += valor_deposito
#         extrato += f"Depósito R$ {valor_deposito:.2f}\n"
#         print("Depósito realizado com sucesso")
#         print(f"Saldo atual: {saldo:.2f}")
#     else:
#         print("Digite um valor válido!")

#     return saldo, extrato


# def sacar(*, valor_saque, saldo, extrato, limite_por_saque, saque, limite_saque):
#     if valor_saque > saldo:
#         print("Saldo insuficiente")
#     elif valor_saque > limite_por_saque:
#         print(f"O limite é de R$ {limite_por_saque} por saque")
#     elif saque >= limite_saque:
#         print("O limite de saques diario é de 3 saques")
#     elif valor_saque > 0:
#         saldo -= valor_saque
#         extrato += f"Saque R$ {valor_saque:.2f}\n"
#         print("Saque realizado com sucesso")
#         print(f"Saldo atual: {saldo:.2f}")
#         saque += 1
#     else:
#         print("Digite um valor válido")

#     return saldo, extrato, saque


# def extrato(saldo, *, extrato):

#     print("\n-----------------------Extrato-----------------------")
#     print("Não foram realizadas movimentações." if not extrato else extrato)
#     print(f"\n Saldo: R$ {saldo:.2f}")
#     print("-------------------------------------------------------")

#     return


# def criar_usuario(usuarios):
#     cpf = input("informe o CPF(somente numeros): ")
#     usuario = filtrar_usuario(cpf, usuarios)

#     if usuario:
#         print("Já existe usuario com este CPF")
#         return

#     nome = input("Digite seu nome: ")
#     data_nascimento = input("Digite saua data de nascimento(Formato dd/mm/aaaa): ")
#     endereco = input(
#         "Digite seu endereço: Logradouro, Numero, Bairro, Cidade - sigla estado: "
#     )

#     usuarios.append(
#         {
#             "nome": nome,
#             "data_nascimento": data_nascimento,
#             "cpf": cpf,
#             "endereco": endereco,
#         }
#     )
#     print("Usuario criado com sucesso")


# def filtrar_usuario(cpf, usuarios):
#     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
#     return usuarios_filtrados[0] if usuarios_filtrados else None


# def criar_conta(agencia, numero_conta, usuarios):
#     cpf = input("informe o CPF(somente numeros): ")
#     usuario = filtrar_usuario(cpf, usuarios)

#     if usuario:
#         print("Conta criada com sucesso!")
#         return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
#     print("Usuario não encontrado")


# def listar_contas(contas):
#     for conta in contas:
#         linha = f"""
#         Agência: {conta["agencia"]}
#         Conta:  {conta["numero_conta"]}
#         Titular: {conta["usuario"]["nome"]}
#         """
#         print("=" * 100)
#         print(linha)


# menu = """
# [1] - Depositar
# [2] - Sacar
# [3] - Extrato
# [4] - Cadastrar usuario
# [5] - Criar conta
# [6] - Listar contas
# [0] - Sair
# """
# LIMITE_SAQUE = 3
# NUMERO_AGENCIA = "0001"

# saldo_conta = 0
# limite = 500
# extrato_transacoes = ""
# numero_saques = 0
# usuarios = []
# contas = []

# while True:

#     opcao = int(input(menu))
#     if opcao == 1:
#         valor = float(input("Digite o valor do depósito: "))
#         retorno_deposito = depositar(valor, saldo_conta, extrato_transacoes)
#         saldo_conta = retorno_deposito[0]
#         extrato_transacoes = retorno_deposito[1]

#     elif opcao == 2:
#         valor = float(input("Digite o valor do saque: "))
#         retorno_saque = sacar(
#             valor_saque=valor,
#             saldo=saldo_conta,
#             extrato=extrato_transacoes,
#             limite_por_saque=limite,
#             saque=numero_saques,
#             limite_saque=LIMITE_SAQUE,
#         )
#         saldo_conta = retorno_saque[0]
#         extrato_transacoes = retorno_saque[1]
#         numero_saques = retorno_saque[2]

#     elif opcao == 3:
#         extrato(saldo_conta, extrato=extrato_transacoes)

#     elif opcao == 4:
#         criar_usuario(usuarios)

#     elif opcao == 5:
#         numero_conta = len(contas) + 1
#         conta = criar_conta(NUMERO_AGENCIA, numero_conta, usuarios)

#         if conta:
#             contas.append(conta)

#     elif opcao == 6:
#         listar_contas(contas)


#     elif opcao == 0:
#         break
#     else:
#         print("Operação inválida!")

# Refatoração 02

import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu():

    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tNova conta
    [6]\tListar contas
    [0]\tSair
    => """
    return int(input(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco
    )

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            depositar(clientes)

        elif opcao == 2:
            sacar(clientes)

        elif opcao == 3:
            exibir_extrato(clientes)

        elif opcao == 4:
            criar_cliente(clientes)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 0:
            break

        else:
            print(
                "\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@"
            )


main()
