class Product:
    def __init__(self, name, quantity, price):
        if not name:
            raise ValueError("Product cannot be empty")
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative")

        self.name = name
        self.quantity = quantity
        self.price = price
        self.active = True

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity  # setting the new amount

        if self.quantity == 0:
            self.active = False  # deactivate the product if 0 amount

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            raise ValueError("Your requested quantity is too high")
        total_price = quantity * self.price
        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        return total_price


class MacBookAirM2(Product):
    def __init__(self):
        super().__init__("MacBook Air M2", 100, 1450.00)


class BoseQuietComfortEarbuds(Product):
    def __init__(self):
        super().__init__("Bose QuietComfort Earbuds", 500, 250.00)


class Store:
    def __init__(self, products=None):
        if products is None:
            self.list_products = []
        else:
            self.list_products = products

    def add_product(self, product):
        self.list_products.append(product)

    def remove_product(self, product):
        if product in self.list_products:
            self.list_products.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = sum(product.get_quantity() for product in self.list_products)
        return total_quantity

    def get_all_products(self) -> list:
        return [product for product in self.list_products if product.is_active()]

    def order(self, shopping_list) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            if product in self.list_products and quantity <= product.get_quantity():
                total_price += product.buy(quantity)
        return total_price

    def show_list_products(self):
        for product in self.list_products:
            product.show()
