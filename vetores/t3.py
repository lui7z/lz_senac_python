vt1 = []
vt2 = []
vt3 = []
x = 0
y = 0

for x in range(10):
    vt1.append(int(input("Type 20 Numbers: ")))

for y in range(10):
    vt2.append(int(input("Type 20 Numbers: ")))

for x, y in zip(vt1, vt2):
    vt3.append(x)
    vt3.append(y)
print(vt3)
