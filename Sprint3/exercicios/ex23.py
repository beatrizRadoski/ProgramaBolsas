class Calculo:
    
    def soma(self,x,y):
        self.x = x
        self.y = y
        
        return x + y
        
    def subtracao(self,x,y):
        self.x = x 
        self.y = y
        
        if x - y >= 0:
            return x - y
        else:
            return 'Resultados negativos não são permitidos'
            
calculo = Calculo()

print(f'Somando: {calculo.soma(4,5)}')
print(f'Subtraindo: {calculo.subtracao(4,5)}')