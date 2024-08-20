class Product:
    """
    Represents a product in the store.

    :param name: Name of the product.
    :param quantity: Quantity of the product in stock.
    :param price: Price of the product.
    """

    def __init__(self, name, quantity, price):
        if not name:
            raise ValueError("Product name cannot be empty")
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative")

        self.name = name
        self.quantity = quantity
        self.price = price
        self.active = True

    def get_quantity(self) -> int:
        """
        Returns the current quantity of the product.

        :return: Quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity of the product and deactivates it if the quantity is zero.

        :param quantity: New quantity of the product.
        """
        if quantity < 0:
            raise ValueError("Quantity must be non-negative")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Checks if the product is active (i.e., has quantity greater than zero).

        :return: True if the product is active, otherwise False.
        """
        return self.active

    def deactivate(self):
        """
        Deactivates the product, marking it as inactive.
        """
        self.active = False

    def __str__(self):
        """
        Returns a string representation of the product.
        """
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """
        Processes the purchase of the product by reducing its quantity and 
        calculating the total price.

        :param quantity: The quantity of the product to buy.
        :return: The total price for the purchased quantity.
        :raises ValueError: If the requested quantity is greater than the available quantity.
        """
        if quantity > self.quantity:
            raise ValueError("Requested quantity exceeds available stock")
        
        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        
        return total_price
