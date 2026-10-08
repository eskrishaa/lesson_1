#List17
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

print(sorted(a))
print(a)  

#List19
n = int(input())
s = []
for i in range(n):
    s.append(input())

print(sorted(s, key=len))
print(max(s, key=len))

#List21
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

pos = [x for x in a if x > 0]  
print(pos)
print(len(pos))

#List22
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())

mult = [x * d for x in a]          
equal = [x for x in a if x == d]   
print(mult)
print(len(equal))

#List23
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

print(sorted(a, key=abs, reverse=True))

#List25
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

b = sorted(a, reverse=True)   
print(b[1]) 

#List26
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

avg = sum(a) / len(a)                   
big = [x for x in a if x > avg]          
print(big)
print(avg)

#List28
n = int(input())
s = []
for i in range(n):
    s.append(input())
letter = input()

found = [x for x in s if x[0] == letter]
print(found)

#List29
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())

b = sorted(a, reverse=True)   
print(b[:k])

#List30
n = int(input())
s = []
for i in range(n):
    s.append(input())

lengths = [len(x) for x in s]      
print(lengths)
print(sum(lengths)) 