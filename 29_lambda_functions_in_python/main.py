add = lambda x, y: x + y
"""
Funções lambda (funções sem nome) possuem 4 partes:

1st -> palavra lambda
2nd -> lista de parâmetros
3rd -> : (cólon)
4th -> valor de retorno
"""

print(add(5, 7))

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
d = list(map(lambda x: x * 2, sequence))
#necessário converter map para list, pois map sempre retornará um objeto

print(doubled)
print(d)

"""
    output terminal:
    
    12
    [2, 6, 10, 18]
    [2, 6, 10, 18]

"""