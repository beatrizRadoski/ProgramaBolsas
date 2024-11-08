from datetime import datetime

nome = 'Beatriz'

idade = 21

idade_que_falta_para_100 = 100 - idade

ano_atual = datetime.now().year

ano_que_fara_100 = ano_atual + idade_que_falta_para_100 

print(ano_que_fara_100)