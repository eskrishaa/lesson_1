#while2
a = float(input("A = "))
b = float(input("B = "))
count = 0
length = a
while length >= b:
    length -= b
    count += 1
print("Количество отрезков:", count)

#while4
n = int(input("N = "))
rest = n
while rest % 3 == 0:
    rest //= 3
print(rest == 1)

#while5
n = int(input("N = "))
k = 0
while n > 1:
    n //= 2
    k += 1
print("K =", k)

#while6
n = int(input("N = "))
result = 1.0
k = n
while k > 0:
    result *= k
    k -= 2
print("N!! =", result)

#while7
n = int(input("N = "))
k = 1
while k * k <= n:
    k += 1
print("K =", k)

#while9
n = int(input("N = "))
power = 1
k = 0
while power <= n:
    power *= 3
    k += 1
print("K =", k)

#while10
n = int(input("N = "))
power = 1
k = 0
while power * 3 < n:
    power *= 3
    k += 1
print("K =", k)

#while12
n = int(input("N = "))
total = 0
k = 0
while total + (k + 1) <= n:
    k += 1
    total += k
print("K =", k)
print("Сумма =", total)

#while13
a = float(input("A = "))
total = 0.0
k = 0
while total <= a:
    k += 1
    total += 1 / k
print("K =", k)
print("Сумма =", total)

#while14
a = float(input("A = "))
total = 0.0
k = 0
while total + 1 / (k + 1) < a:
    k += 1
    total += 1 / k
print("K =", k)
print("Сумма =", total)