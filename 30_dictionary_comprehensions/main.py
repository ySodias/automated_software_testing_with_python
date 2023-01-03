users = [
    (0, "yuri", "password"),
    (1, "leia", "1345")
]

username_mapping = {user[1]: user for user in users}

print(username_mapping)
"""
    output terminal:
    
    {'yuri': (0, 'yuri', 'password'), 'leia': (1, 'leia', '1345')}

"""