prev = int(input("Enter the previous gas meter reading "))
curr = int(input("Enter the current gas meter reading "))
if curr >= prev:
    used = curr - prev
else:
    used = (10000 - prev) + curr
if used <= 300:
    pay = 21
elif used <= 600:
    pay = 21 + (used - 300) * 0.06
elif used <= 800:
    pay = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    pay = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025
avg_price = pay / used

print(f"{'Previous':>8} {'Current':>6} {'Used':>6} {'To pay':>7} {'Avg. price m^3':>13}")
print(f"{prev:>8} {curr:>6} {used:>6} {pay:>7.2f} {avg_price:>12.2f}")

