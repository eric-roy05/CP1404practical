TOTAL_COST = 0
number_of_items = int(input(("How many items: ")))
for i in range(number_of_items):
    price_of_items = float(input("Price of item: "))
    TOTAL_COST += price_of_items

total_cost_with_discount = TOTAL_COST - TOTAL_COST * 0.10
print(f"Total price for {number_of_items} items is ${total_cost_with_discount:.2f}")
