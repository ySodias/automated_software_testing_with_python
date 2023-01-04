import functools

user = {"username": "jose", "access_level": "admin"}


def make_secure(function):
    @functools.wraps(function)
    def secure_function(*args, **kwargs):
        """
        É necessário passar parâmetros para a função chamada no decorator,
        pois a função que recebe o decorator é uma cópia da função primária

        function() é uma cópia de get_admin_password()

        Observação: é melhor usar *args e **kwargs em decorators
        para conseguir reutilizar o decorator em outras funções
        """
        if user["access_level"] == "admin":
            return function(*args, **kwargs)
    return secure_function
@make_secure
def get_admin_password(panel):
    if panel == 'admin':
        return '1234'
    else:
        return 'super_secure_password'

print(get_admin_password('admin'))