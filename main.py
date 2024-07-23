from products import Product, MacBookAirM2, BoseQuietComfortEarbuds, Store

bose = BoseQuietComfortEarbuds()
mac = MacBookAirM2()

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()

new_list = [bose, mac]
store = Store(new_list)

pixel = Product("Google Pixel 7", 250, 500)
store.add_product(pixel)
store.show_list_products()  # method calling

print(f"Total quantity in store: {store.get_total_quantity()}")

bose = BoseQuietComfortEarbuds()
mac = MacBookAirM2()

store = Store([bose, mac])
price = store.order([(bose, 5), (mac, 30), (bose, 10)])
print(f"Order cost: {price} dollars.")

store.show_list_products()  # correct methode calling


product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
]

store = Store(product_list)
products = store.get_all_products()
print(store.get_total_quantity())
print(store.order([(products[0], 1), (products[1], 2)]))
