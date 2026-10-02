#for2
a = int(input())
b = int(input())
count = 0
for i in range(a, b + 1):
    print(i)
    count += 1
print("количество:",count)

#for4
price = float(input())
for i in range(1, 11):
    print(price * i)

#for5
price = float(input())
for i in range(1, 11):
    weight = i / 10
    print(price * weight)

#for6
price = float(input())
for i in range(12, 21, 2):
    weight = i / 10
    print(price * weight)

#for8
a = int(input())
b = int(input())
total = 1
for i in range(a, b + 1):
    total *= i
print(total)

#for9
a = int(input())
b = int(input())
total = 0
for i in range(a, b + 1):
    total += i ** 2
print(total)

#for11
n = int(input())
total = 0
for i in range(n, 2 * n + 1):
    total += i ** 2
print(total)

#fpr12
n = int(input())
product = 1.0
for i in range(1, n + 1):
    product *= 1 + i / 10
print(product)

#for13
n = int(input())
total = 0.0
sign = 1
for i in range(1, n + 1):
    total += sign * (1 + i / 10)
    sign = -sign
print(total)

#for15
a = float(input())
n = int(input())
power = 1.0
for _ in range(n):
    power *= a
print(power)
