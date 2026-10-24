# Class2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shift(self, dx, dy):
        self.x += dx
        self.y += dy

x = int(input())
y = int(input())
dx = int(input())
dy = int(input())

p = Point(x, y)
p.shift(dx, dy)
print(p.x)
print(p.y)

# Class4
class Potion:
    def __init__(self, name, price, heal):
        self.name = name
        self.price = price
        self.heal = heal

    def describe(self):
        return f"{self.name}: {self.price} gold, +{self.heal} health"

name = input()
price = int(input())
heal = int(input())

p = Potion(name, price, heal)
print(p.describe())

# Class6
class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, name, qty):
        self.items[name] = self.items.get(name, 0) + qty

    def total(self):
        return sum(self.items.values())

inv = Inventory()
for i in range(3):
    name = input()
    qty = int(input())
    inv.add(name, qty)

print(inv.total())

# Class7
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

x = int(input())
y = int(input())

p = Point(x, y)
print(p)

# Class8
class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def to_dict(self):
        return {
            "name": self.name,
            "health": self.health,
            "damage": self.damage
        }

    @staticmethod
    def from_dict(data):
        return Hero(data["name"], data["health"], data["damage"])

name = input()
health = int(input())
damage = float(input())

h1 = Hero(name, health, damage)
data = h1.to_dict()
h2 = Hero.from_dict(data)

print(h2.health)