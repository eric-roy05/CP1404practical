import random

# Constants
MIN_PRICE = 1.0
MAX_PRICE = 100.0
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
INITIAL_PRICE = 10.0
OUTPUT_FILE = "stock_simulation_output.txt"

# Initialization
price = INITIAL_PRICE
number_of_days = 0

# Open the file for writing
out_file = open(OUTPUT_FILE, 'w')

# Output initial price to the file
print(f"Day {number_of_days}: ${price:,.2f}", file=out_file)

# Simulation loop
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise, it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    number_of_days += 1

    # Output current day's price to the file
    print(f"Day {number_of_days}: ${price:,.2f}", file=out_file)

out_file.close()



