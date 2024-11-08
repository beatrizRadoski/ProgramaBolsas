class Passaro:
    
    def __init__(self):
        pass 
    
    
    def voar(self):
        return 'Voando...'
        
    
    def emitir_som(self):
        pass


class Pato(Passaro):
    def __init__(self):
        super().__init__()
        
    
    def voar(self):
        return super().voar()
        
    def emitir_som(self):
        return '''Pato emitindo som...
Quack Quack'''
                  
                  

class Pardal(Passaro):
    def __init__(self):
        super().__init__()
        
    
    def voar(self):
        return super().voar()
        
        
    def emitir_som(self):
        return '''Pardal emitindo som...
Piu Piu'''
    
pato = Pato()
pardal = Pardal()

print("Pato")
print(pato.voar())
print(pato.emitir_som())
print('Pardal')
print(pardal.voar())
print(pardal.emitir_som())