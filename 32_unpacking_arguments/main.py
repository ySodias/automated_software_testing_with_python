def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(1,2,3))


def add(x, y):
    return x + y

nums = [3,5]
nums_dict = {'x': 15, 'y': 25}

print(add(*nums))
print(add(**nums_dict)) #quando as keys do dict são iguais aos parâmetros da função

