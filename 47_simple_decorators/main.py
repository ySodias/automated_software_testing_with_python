user = {"username": "jose", "access_level": "guest"}

def get_admin_password():
    return '1234'

def make_secure(function):
    def secure_function():
        if user["access_level"] == "admin":
            return function()
    return secure_function

get_admin_password = make_secure(get_admin_password)

print(get_admin_password())