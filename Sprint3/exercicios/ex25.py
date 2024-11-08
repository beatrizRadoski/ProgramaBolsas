class Aviao:
    
    def __init__(self, modelo, velocidade_maxima, capacidade, cor='Azul'):
        self.cor = cor
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        

aviao1 = Aviao('BOIENG456','1500 km/h','400')
aviao2 = Aviao('Embraer Praetor 600','863 km/h','14')
aviao3 = Aviao('Antonov An-2','258 km/h','12')

lista = []
lista.append(aviao1)
lista.append(aviao2)
lista.append(aviao3)

for aviao in lista:
    print(f'''O avião de modelo {aviao.modelo} 
possui uma velocidade máxima de {aviao.velocidade_maxima}, 
capacidade para {aviao.capacidade} e é da cor {aviao.cor}''')