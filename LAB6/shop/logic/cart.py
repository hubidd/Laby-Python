class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def total_price(self):
        return sum(p.price for p in self.products)

    def __len__(self):
        return len(self.products)

    def __contains__(self, product):
        return product in self.products

    def __str__(self):
        items = [str(p) for p in self.products]
        return "Zawartość koszyka:\n" + "\n".join(items) + f"\nSuma całkowita: {self.total_price()}"