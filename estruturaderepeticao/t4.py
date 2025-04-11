A = 80000
txaA = 0.03
B = 200000
txaB = 0.015
ages = 0

for i in range(1000):
    if A >= B:
        break
    A *= (1 + txaA)
    B *= (1 + txaB)
    ages += 1

print(f"The County 'A' needs {ages} years to reach at the country 'B' Population")