# Dict2
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

k = input()
if k in d:
    print(d[k])
else:
    print("нет такого ключа")

# Dict3
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

k = input()
print(d.get(k, 0))

# Dict5
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

k = input()
d.pop(k, None)
print(len(d))

# Dict7
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

best = None
for key in d:
    if best is None or d[key] > d[best]:
        best = key

print(best)

# Dict8
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

v = int(input())
print(v in d.values())

# Dict9
n = int(input())
d1 = {}
for i in range(n):
    key = input()
    value = int(input())
    d1[key] = value

m = int(input())
d2 = {}
for i in range(m):
    key = input()
    value = int(input())
    d2[key] = value

d1.update(d2)
print(len(d1))

for key in d1:
    if key in d2:
        print(d1[key])
        break

# Dict12
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

inv = {}
for key, value in d.items():
    inv[value] = key

for value, key in inv.items():
    print(f"{value}: {key}")

# Dict13
n = int(input())
d = {}
for i in range(n):
    name = input()
    price = int(input())
    qty = int(input())
    d[name] = [price, qty]

total_cost = 0
best_name = None
best_cost = 0

for name in d:
    price, qty = d[name]
    cost = price * qty
    total_cost += cost
    if cost > best_cost:
        best_cost = cost
        best_name = name

print(total_cost)
print(best_name)

# Dict14
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

v = int(input())

for key in list(d):
    if d[key] < v:
        del d[key]

print(len(d))

# Dict15
n = int(input())
d1 = {}
for i in range(n):
    key = input()
    value = int(input())
    d1[key] = value

m = int(input())
d2 = {}
for i in range(m):
    key = input()
    value = int(input())
    d2[key] = value

ignored = 0
for key, value in d2.items():
    if key in d1:
        ignored += 1
    else:
        d1[key] = value

print(len(d1))
print(ignored)
