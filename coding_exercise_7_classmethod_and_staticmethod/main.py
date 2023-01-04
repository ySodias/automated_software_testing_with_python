class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __repr__(self):
        return f"<Store {self.name}, { self.items}>"

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(f"{store} - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return f"{store.name}, total stock price: {store.stock_price()}"

store = Store("Test")
store.add_item(name='Teste3', price=50)
print(store.franchise("Teste2"))
print(store.store_details(store))
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)
#print(store)
#print(store2)