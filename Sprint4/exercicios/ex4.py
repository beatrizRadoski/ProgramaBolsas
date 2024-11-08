def calcular_valor_maximo(operadores,operandos):
    
    operacoes = {
        '+' : lambda x,y: x+y,
        '-' : lambda x,y: x-y,
        '*' : lambda x,y: x*y,
        '/' : lambda x,y: x/y if y != 0 else float('inf'),
        '%' : lambda x,y: x%y if y != 0 else float('inf')
    }
    
    resultados = list(map(lambda op_and_operand: operacoes[op_and_operand[0]](op_and_operand[1][0], op_and_operand[1][1]), zip(operadores, operandos)))
    
    return max(resultados)
    
operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

resultado = calcular_valor_maximo(operadores,operandos)
print(resultado)