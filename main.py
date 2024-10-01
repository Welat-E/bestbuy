from products import Product, LimitedProduct, NonStockedProduct
from store import Store
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount


def start(store):
    """
    Display the store menu and process user input to perform actions such as
    listing products, showing total amount, making an order, or quitting the program.

    :param store: Store object containing the list of products.
    """
    while True:
        print("\nStore Menu\n----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Please choose a number: ")

        if choice == "1":
            store.show_list_products()
        elif choice == "2":
            total_quantity = store.get_total_quantity()
            print(f"Total quantity in store: {total_quantity}")
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please try again.")


def make_order(store):
    """
    Facilitate the ordering process by allowing users to select products and specify quantities.
    Validate inputs and notify the user if the requested quantity exceeds available stock.

    :param store: Store object containing the list of products.
    """
    shopping_list = []
    while True:
        print("\n------")
        for i, product in enumerate(store.list_products, start=1):
            print(
                f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}"
            )
        print("------")
        product_number = input("Which product # do you want? (or 'done' to finish): ")

        if product_number.lower() == "done" or product_number == "":
            break

        try:
            product_index = int(product_number) - 1
            if 0 <= product_index < len(store.list_products):
                quantity = int(
                    input(
                        f"Enter the quantity for {store.list_products[product_index].name}: "
                    )
                )

                # Check if the requested quantity is available
                if quantity > store.list_products[product_index].get_quantity():
                    print(
                        f"Requested quantity exceeds available stock for {store.list_products[product_index].name}."
                    )
                else:
                    shopping_list.append((store.list_products[product_index], quantity))
            else:
                print("Invalid product number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    total_price = store.order(shopping_list)
    print(f"Order cost: {total_price} dollars.")


def main():
    """
    Main function to setup initial stock of inventory and start the store program.
    """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
