#Boolean2
A = int(input("A: "))
print(A % 2 != 0)

#Boolean3
A = int(input("A: "))
print(A % 2 == 0)

#Boolean4
A = int(input("A: "))
B = int(input("B: "))
print(A > 2 or B<=3)

#Boolean5
A = int(input("A: "))
B = int(input("B: "))
print(A >= 0 and B<-2)

#Boolean7
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
print((A < B < C) or (C < B < A))

A = int(input("A: "))
B = int(input("B: "))
print(A % 2 != 0 and B % 2 != 0)

#Boolean9
A = int(input("A: "))
B = int(input("B: "))
print(A % 2 != 0 or B % 2 != 0)

#Boolean10
A = int(input("A: "))
B = int(input("B: "))
count = (A % 2 != 0) + (B % 2 != 0)
print(count == 1)

#Boolean11
A = int(input("A: "))
B = int(input("B: "))
print(A % 2 == B % 2)

#Boolean13
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
print(A > 0 or B > 0 or C > 0)

#Boolean15
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
count = (A > 0) + (B > 0) + (C > 0)
print(count == 2)

#If1
A = int(input('A:'))
if A > 0:
    A += 1
print(A)

#if2
A = int(input('A:'))
if A > 0:
    A += 1
else:
    A -= 2
print(A)

#if4
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
count = (A > 0) + (B > 0) + (C > 0)
print(count)

#If5
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
pos = (A > 0) + (B > 0) + (C > 0)
neg = (A < 0) + (B < 0) + (C < 0)
print("Положительных:", pos)
print("Отрицательных:", neg)
