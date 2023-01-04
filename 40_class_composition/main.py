"""
Herança -> Ocorre quando a classe herda atributos e métodos de outra classe
Composição -> Quando uma classe não depende apenas da classe filha para existir

Pensando com Composição é como “ter” um relacionamento. O Ser Humano “tem” a capacidade amamentar, raciocinar e também “tem” pernas e braços e assim por diante.

Ser Humano = capacidade amamentar + braços + pernas

Já pensando com Herança “é” como uma relação. O Ser Humano “é” um Mamífero, um Carro “é” um Veículo, Maçã “é” uma Fruta e etc.

Ser Humano < Mamífero

link: https://medium.com/opensanca/heran%C3%A7a-ou-composi%C3%A7%C3%A3o-eis-a-quest%C3%A3o-7ce11fad4737#:~:text=A%20HERAN%C3%87A%20%C3%89%20FUNDAMENTAL,%E2%80%9D%2C%20mas%20ainda%20polim%C3%B3rfica).
"""

class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books"

class Book:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("Python 101")
book2 = Book("Python 202")
shelf = BookShelf(book, book2)

print(shelf)