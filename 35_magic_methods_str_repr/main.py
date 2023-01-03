class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """
        :return: retorna string objeto após criado
        """
        return f"Person {self.name}, {self.age} years old"

    def __repr__(self):
        """
        :return: retorna a representação do objeto

        Observação: Não funciona se houver o __str__
        """
        return f"<Person({self.name}, {self.age})>"

bob = Person("bob", 35)
print(bob)