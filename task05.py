class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock


p1 = Product("Smartfon", 12999.99, "electronics", True)
p2 = Product("Muzlatkich", 8999.50, "electronics", False)


print(p1.name, "-", p1.price)
print(p2.name, "-", p2.price)
