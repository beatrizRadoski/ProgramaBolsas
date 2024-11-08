def impressao_parametros(*args,**kwargs):
    for valor in args:
        print(valor)
 
    for chave, valor in kwargs.items():
        print(valor)
        
impressao_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)