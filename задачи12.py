# String2
n = int(input())
print(chr(n))

# String3
c = input()
print(chr(ord(c) - 1))
print(chr(ord(c) + 1))

# String4
n = int(input())
print("".join(chr(ord("A") + i) for i in range(n)))

# String5
n = int(input())
print("".join(chr(ord("z") - i) for i in range(n)))

# String7
s = input()
print(ord(s[0]))
print(ord(s[-1]))

# String8
n = int(input())
c = input()
print(c * n)

# String9
n = int(input())
c1 = input()
c2 = input()
print("".join(c1 if i % 2 == 0 else c2 for i in range(n)))
# String12
s = input()
n = int(input())
stars = "*" * n
print(stars.join(s))

# String14
s = input()
count = 0
for ch in s:
    if "A" <= ch <= "Z":
        count += 1
print(count)

# String15
s = input()
count = 0
for ch in s:
    if ("a" <= ch <= "z") or ("а" <= ch <= "я"):
        count += 1
print(count)
