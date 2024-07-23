from products import Product, Store


def start(store):
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
            print(f"Total quantity in store: {store.get_total_quantity()}")
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please try again.")


def make_order(store):
    shopping_list = []
    while True:
        print("\n------")
        for i, product in enumerate(store.list_products, start=1):
            print(
                f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}"
            )
        print("------")
        product_number = input("Which product # do you want? (or 'done' to finish): ")

        if product_number == "done" or product_number == "":
            break

        try:
            product_index = int(product_number) - 1
            if 0 <= product_index < len(store.list_products):
                quantity = int(
                    input(
                        f"Enter the quantity for {store.list_products[product_index].name}: "
                    )
                )
                shopping_list.append((store.list_products[product_index], quantity))
            else:
                print("Invalid product number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    total_price = store.order(shopping_list)
    print(f"Order cost: {total_price} dollars.")


# setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = Store(product_list)


start(best_buy)
