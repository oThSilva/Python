#O programa deverá solicitar ao usuário informações sobre a conta a ser paga, como o nome do beneficiário, o valor da conta a ser paga e a data de vencimento. Em seguida, o programa fornecerá uma mensagem de confirmação do agendamento com as informações fornecidas. saída deve ser:
#"Pagamento Agendado! Valor: R$ [Valor da Conta], vencimento [Data de Vencimento]."

from datetime import datetime
nome = input('Nome: ')
valor = float(input('Valor a ser depositado: '))
valor_formatado = "{:.0f}".format(valor)
data_vencimento = datetime.strptime(input('Data de vencimento:'),'%d/%m/%Y')
data_formatada = data_vencimento.strftime("%d/%m/%Y")

print(f'Pagamento Agendado! Valor: R$ {valor_formatado}, vencimento {data_formatada}."')

