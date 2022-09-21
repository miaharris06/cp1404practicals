total_price = 0
items = 0
no_of_items = int(input("Number of items: "))
while no_of_items < 0:
    print("Invalid number of items!")
    no_of_items = int(input("Number of items: "))
for i in range(no_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price
    items += 1
if total_price > 100:
    total_price = total_price - total_price * 0.1
print(f"Total price for {items} items is ${total_price:.2f}")
