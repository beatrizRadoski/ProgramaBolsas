def pares_ate(n):
    pares = (num for num in range(2,n+1,2))
    return pares
    
resultado = pares_ate(24)
print(resultado)