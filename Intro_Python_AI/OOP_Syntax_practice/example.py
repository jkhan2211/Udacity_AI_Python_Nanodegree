from shirt import Shirt

shirt_one = Shirt('red', 'S', 'long-sleeve', 25)
shirt_two = Shirt('orange', 'L', 'short-sleeve', 10)
print(shirt_one.price)
print(shirt_one.color)

shirt_two.change_price(45)
print(shirt_two.price)

shirt_one.color = 'yellow'
shirt_one.size = 'L'
shirt_one.price = 45

