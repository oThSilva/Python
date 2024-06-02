# Agora, vamos Adicionar uma funcionalidade à classe UsuarioTelefone para que possa ser verificado o saldo disponível em seu plano. Para essa solução, você pode criar uma classe PlanoTelefone, o seu método de inicialização e encapsular os atributos, 'nome' e 'saldo' dentro da classe. Adicione também um método 'verificar_saldo' para verificar o saldo do plano e uma  'mensagem_personalizada' para gerar uma mensagem personalizada.

# Condições da verificação do saldo:
# - Caso o saldo seja menor do que 10, retorne: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
# - Caso o saldo seja maior ou igual a 50, retorne: "Parabéns! Continue aproveitando seu plano sem preocupações."
# - Caso contrário, retorne: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

# Entrada
# Como entrada, será solicitado o nome, plano (Essencial, Prata, Premium) e saldo atual do cliente.

# Saída
# Mensagem personalizada de acordo o saldo do cliente.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	    Saída
# João          Seu saldo está baixo. Recarregue e use os serviços do seu plano.
# Essencial
# 9

# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':

# TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:

# TODO: Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo:


class UsuarioTelefone:
    def __init__(self, nome_usuario, plano_usuario):
        self.nome_usuario = nome_usuario
        self.plano_usuario = plano_usuario


class PlanoTelefone:
    def __init__(self, nome, saldo):
        self._nome = nome
        self._saldo = saldo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def verificar_saldo(self):

        plano1 = self._saldo < 10
        plano2 = self._saldo >= 50

        if plano1:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif plano2:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

    def mensagem_personalizada(self):
        return self.verificar_saldo()


def main():
    nome_usuario = input("Digite o nome do usuário: ")
    nome_plano = input("Digite o nome do plano: ")
    saldo_inicial = float(input("Digite o saldo inicial do plano: "))

    plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
    usuario = UsuarioTelefone(nome_usuario, plano_usuario)

    mensagem_usuario = plano_usuario.mensagem_personalizada()
    print(mensagem_usuario)


main()
