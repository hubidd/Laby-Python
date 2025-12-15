class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price}"

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, category='{self.category}')"

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.category == other.category

    def __lt__(self, other):
        return self.price < other.price

    def __len__(self):
        return len(self.name)