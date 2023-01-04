import functools

user = {"username": "jose", "access_level": "admin"}


def make_secure(function):
    @functools.wraps(function)
    def secure_function():
        """
        Importante usar a lib functools,
        pois ao usar o decorator o nome da função mudará para o função dentro do decorator caso não use a lib
        :return:
        """
        if user["access_level"] == "admin":
            return function()
    return secure_function
@make_secure
def get_admin_password():
    return '1234'

print(get_admin_password())