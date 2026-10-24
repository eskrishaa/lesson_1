# File1
import os

s = input()
try:
    with open(s, "w", encoding="utf-8") as f:
        pass
    print(True)
except OSError:
    print(False)

# File3
a = float(input())
d = float(input())
name = input()

with open(name, "w", encoding="utf-8") as f:
    for i in range(10):
        f.write(str(a + i * d) + "\n")

# File4
import os

names = [input() for _ in range(4)]
count = 0
for name in names:
    if os.path.exists(name):
        count += 1
print(count)

# File8
name1 = input()
name2 = input()

with open(name1, encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

with open(name2, "w", encoding="utf-8") as f:
    f.write(lines[0] + "\n")
    if len(lines) > 1:
        f.write(lines[-1] + "\n")

# File9
name1 = input()
name2 = input()

if os.path.exists(name1):
    src, dst = name1, name2
else:
    src, dst = name2, name1

with open(src, encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

with open(dst, "w", encoding="utf-8") as f:
    f.write(lines[-1] + "\n")
    if len(lines) > 1:
        f.write(lines[0] + "\n")