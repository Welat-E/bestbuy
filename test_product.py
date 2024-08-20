import pytest
from products import Product


def test_create_product():
    # Test that creating a normal product works.
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active()


def test_create_product_invalid_name():
    # Test that creating a product with an empty name raises a ValueError.
    with pytest.raises(ValueError, match="Product name cannot be empty"):
        Product("", price=1450, quantity=100)


def test_create_product_negative_price():
    # Test that creating a product with a negative price raises a ValueError.
    with pytest.raises(ValueError, match="Price and quantity must be non-negative"):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_product_becomes_inactive():
    # Test that a product becomes inactive when its quantity reaches 0.
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)
    assert not product.is_active()


def test_product_purchase_modifies_quantity():
    # Test that purchasing a product modifies its quantity and returns the correct total price.
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(2)
    assert product.quantity == 98
    assert total_price == 1450 * 2


def test_buying_larger_quantity_than_exists():
    # Test that buying a quantity larger than what is available raises a ValueError.
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError, match="Requested quantity exceeds available stock"):
        product.buy(200)
