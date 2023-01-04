"""
Em Python todas as coisas são mutáveis, pois todas as coisas são objetos

A menos que n seja possível de mudar as propriedades do objeto (exemplo: tuples)

Python não recria números inteiros já criados, números inteiros são imutáveis

exemplo:

a = 5
b = 5

Ambos estão alocados no mesmo espaço de memória
"""

a = []
b = a

print(id(a))
print(id(b))