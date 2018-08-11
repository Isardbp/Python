def apply_descount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

shoes = {'name' : 'Fancy Shoes', 'price' : 14900}

print(apply_descount(shoes, 2.00))
