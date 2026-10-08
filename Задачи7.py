#List2
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())

print(a[k])
print(a[-1])
print(k)

#List3
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

total = 0
product = 1
for i in range(len(a)):
    total += a[i]
    if i % 2 == 0:
        product *= a[i]

print(total)
print(product)

#list5
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())

a.append(d)
print(a)
print(len(a))

#List7
n = int(input())
a = []
for i in range(n):
    a.append(int(input))

b = a[::-1]
print(a)
print(b)

#List9
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

total = 0
for x in a:
    total += x
avg = total / n

count = 0
for x in a:
    if x > avg:
        print(x)
        count += 1
print(count)

#List10
n = int(input())
a = []
for i in range(n):
    a.append(input())

imax = 0
imin = 0
for i in range(len(a)):
    if len(a[i]) > len(a[imax]):
        imax = i
    if len(a[i]) < len(a[imin]):
        imin = i

print(a[imax], len(a[imax]))
print(a[imin], len(a[imin]))

#list12
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())

a.insert(k, 0)
print(a)
print(len(a))

#List13
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

removed = a.pop()
print(removed)
print(a)

#List14
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())

print(a.count(d))
if d in a:
    print(a.index(d))
else:
    print(-1)

#List15
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

total = 0
for i in range(1, len(a), 2):
    print(a[i])
    total += a[i]
print(total)
