class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name

        if price < 0:
            raise ValueError("Price cannot be negative")
        self.price = price

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity

        self.active = True

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity  # setting the new amount

        if self.quantity == 0:
            self.active = False  # deactivate the product if 0 amount

    def is_active(self) -> bool:
        if self.active == True:
            return True
        else:
            return False

    def active(self):
        return self.name == True

    def deactivate(self):
        return self.name == False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            raise ValueError("Your requested quantity is too high")
        total_price = quantity * self.price
        self.quantity -= quantity
        return total_price


class MacBookAirM2(Product):
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price)
        self.price = 1450, 00
        self.name = "MacBook Air M2"
        self.quantity = 850


class BoseQuietComfortEarbuds(Product):
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price)
        self.price = 250, 00
        self.name = "Bose QuietComfort Earbuds"
        self.quantity = 850


# Setter function for quantity. If quantity reaches 0, deactivates the product.
