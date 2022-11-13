def delivery_price(count):
    return 10.95 + (2.95 * (count - 1))


print(delivery_price(int(input())))
