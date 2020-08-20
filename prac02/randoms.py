"""
Q1) 5, 20
Q2) 3, 9
Q3) 2.5, 5.5
"""
import random
print(random.randint(1, 100))

PRICE_RANGE_MINIMUM = 1
PRICE_RANGE_MAXIMUM = 100
PERCENTAGE_INCREASE = 0.825
PERCENTAGE_DECREASE = 0.95
OUTPUT_FILE = "prac02.txt"
day = 0
stock_price = 10.0
out_file = open(OUTPUT_FILE, "w")
print(f"Starting price: ${stock_price}", file=out_file)
while PRICE_RANGE_MINIMUM < stock_price < PRICE_RANGE_MAXIMUM:
    up_or_down = random.randint(1, 2)
    if up_or_down == 1:
        price_percentage = random.uniform(PERCENTAGE_INCREASE, 1)
        stock_price /= price_percentage
    else:
        price_percentage = random.uniform(PERCENTAGE_DECREASE, 1)
        stock_price *= price_percentage
    day += 1
    print(f"On day {day} price is: ${stock_price:,.2f}", file=out_file)
out_file.close()
