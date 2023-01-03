def named(**kwargs):
    print(kwargs)

named(name="bob", age=25)

named_lambda = (lambda **kwargs: kwargs)(name='yuri', age=25)
print(named_lambda)

"""
    terminal output:
    
    {'name': 'bob', 'age': 25}
    {'name': 'yuri', 'age': 25}
"""