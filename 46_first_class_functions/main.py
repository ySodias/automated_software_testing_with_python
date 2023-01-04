def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 5, operator=divide)
print(result)


def search(sequence, expected, finder):
    for element in sequence:
        if finder(element) == expected:
            return element
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Yuri", "age": 22},
    {"name": "Danilo", "age": 28}
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, 'Yuri', get_friend_name))