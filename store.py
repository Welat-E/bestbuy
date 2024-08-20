class Store:
    def __init__(self, product_list):
        self.list_products = product_list

    def show_list_products(self):
        for product in self.list_products:
            print(product)

    def get_total_quantity(self):
        return sum(product.quantity for product in self.list_products)

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            if product.quantity >= quantity:
                product.set_quantity(product.quantity - quantity)
                total_price += product.price * quantity
            else:
                print(f"Not enough stock for {product.name}.")
        return total_price
