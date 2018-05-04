# Modulo de Calculos

def fatorial(n):
    '''Retorna o fatorial de um número.'''
    fat = 1
    for i in range(2,n+1):
        fat = fat * i
    return fat

def fibonacci(limite):
    '''Retorna o primeiro número de Fibonnaci maior do que o valor limite.'''
    x, y = 0, 1
    while True:
        x, y = y, x+y
        if y > limite:
            break
    return y
        
