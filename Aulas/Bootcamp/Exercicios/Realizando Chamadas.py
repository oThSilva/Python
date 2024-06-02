# Vamos agora, adicionar uma funcionalidade à classe UsuarioTelefone, que realizar chamadas para outros usuários. Cada chamada terá uma duração em minutos e o custo será deduzido do saldo do usuário, suponha o custo de $0.10 por minuto. Você pode criar um método fazer_chamada que vai permitir que o usuário faça a chamada, ele vai receber o destinatario e duracao como parâmetros. Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano', além de adicionar o método deduzir_saldo para deduzir o valor do saldo do plano e depois retorne uma mensagem adequada como mostra no exemplo a baixo.

# Entrada
# Número do usuário, número do telefone, saldo inicial, número do destinatário e a duração da chamada em minutos.

# Saída
# Mensagem indicando o sucesso da chamada ou saldo insuficiente para fazer a chamada.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	        Saída

# Rodrigo           Chamada para (33) 93333-3333 realizada com sucesso. Saldo: $4.00
# (00) 90000-0000
# 10.00
# (33) 93333-3333
# 60

# Yule              Chamada para (00) 90000-0000 realizada com sucesso. Saldo: $6.00
# (11) 91111-1111
# 30.00
# (00) 90000-0000
# 240

# Amelia            Saldo insuficiente para fazer a chamada.
# (33) 93333-3333
# 10.00
# (11) 91111-1111
# 120


class Plano:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def custo_chamada(self, duracao):
        return 0.10 * duracao

    def deduzir_saldo(self, valor):
        self._saldo -= valor


class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self._nome = nome
        self._numero = numero
        self._plano = plano

    @property
    def nome(self):
        return self._nome

    @property
    def numero(self):
        return self._numero

    @property
    def plano(self):
        return self._plano

    def fazer_chamada(self, destinatario, duracao):
        custo = self._plano.custo_chamada(duracao)
        if self._plano.saldo > custo:
            self._plano.deduzir_saldo(custo)
            return f"Chamada para {destinatario} concluída com sucesso. Saldo restante: ${self._plano.saldo:.2f}"
        else:
            return "Saldo insuficiente para realizar a chamada."


class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


def main():
    nome = input("Digite o nome do usuário: ")
    numero = input("Digite o número do telefone: ")
    saldo_inicial = float(input("Digite o saldo inicial: "))

    usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
    destinatario = input("Digite o número do destinatário: ")
    duracao = int(input("Digite a duração da chamada em minutos: "))

    print(usuario_pre_pago.fazer_chamada(destinatario, duracao))


main()
