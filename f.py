def price_taxi(distance):
    metres = distance * 1000
    price = int((metres / 140)) * 0.25 + 4
    return price


print(price_taxi(3))
