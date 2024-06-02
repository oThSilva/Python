from datetime import datetime

print(datetime.now())
print(datetime.now().day)

#criar uma data
data_exemplo = datetime(2024, 2, 11)
print(data_exemplo)
print(type(data_exemplo))

#convertendo para datetime(não precisa mais)

data = datetime.strptime(input('Qual é a data? '), '%d/%m/%Y')
print(data)
print(type(data))

#para calcular o intervalo entre datas 
data_atual = datetime.now()
prazo = data_exemplo - data_atual
print(prazo.days)

#strptime (string parse time)para converter uma string em um objeto 'datetime'
data_string = "2022-01-11 08:30:00"
formato = "%Y-%m-%d %H:%M:%S"
data_objeto = datetime.strptime(data_string, formato)
print(data_objeto)
#strftime (string format time)para formatar um objeto 'datetime' como uma string
data_objeto = datetime(2022, 1, 11, 8, 30)
formato = "%Y-%m-%d %H:%M:%S"
data_formatada = data_objeto.strftime(formato)
print(data_formatada)



#Desafio
dia_do_aniversario = datetime(2024, 2, 24)
dias_pro_aniversario = dia_do_aniversario - datetime.now()
print(dia_do_aniversario)