from models.product import Product
from logic.cart import Cart

if __name__ == "__main__":
    p1 = Product("Laptop", 3500, "electronics")
    p2 = Product("Monitor", 1200, "electronics")
    p3 = Product("Jabłko", 2.5, "food")
    p4 = Product("Laptop", 4000, "electronics")

    print(p1 == p4)
    print(p3 < p1)
    print(len(p1))

    products_list = [p1, p2, p3]
    products_list.sort()
    print(products_list)

    cart = Cart()
    cart.add_product(p1)
    cart.add_product(p3)

    print(len(cart))
    print(p1 in cart)
    print(cart.total_price())
    print(cart)