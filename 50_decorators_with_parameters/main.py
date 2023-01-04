import functools

user = {"username": "jose", "access_level": "admin"}

def make_secure(access_level):
    def decorator(function):
        @functools.wraps(function)
        def secure_function(*args, **kwargs):
            """
            """
            if user["access_level"] == access_level:
                return function(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}"
        return secure_function
    return decorator
@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"

print(get_admin_password())