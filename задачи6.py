№Err2
a = int(input("A = "))
b = int(input("B = "))

try:
    result = a / b
except ZeroDivisionError:
    print("Делить на ноль нельзя")
else:
    print(f"{result:.1f}")

№Err5
word = input("Строка: ")
index = int(input("Индекс: "))

try:
    print(word[index])
except IndexError:
    print("Нет такого символа")

№Err6
word = input("Строка: ")

try:
    index = int(input("Индекс: "))
    print(word[index])
except ValueError:
    print("Ошибка ввода")
except IndexError:
    print("Нет такого символа")

#Err7
while True:
    try:
        number = int(input())
        break
    except ValueError:
        print("Это не число. Попробуй ещё:")

print(number)

#Err9
try:
    age = int(input("Возраст: "))
    if age < 0 or age > 120:
        raise ValueError("Возраст вне допустимого диапазона")
except ValueError as e:
    print("Отклонено:", e)
else:
    print("Принято:", age)

#Err11
try:
    a = float(input("A = "))
    b = float(input("B = "))
    result = a / b
except (ValueError, ZeroDivisionError):
    print("Посчитать не удалось")
else:
    print(f"{result:.2f}")

#Err12
try:
    number = int(input("Число: "))
except ValueError as e:
    print(e)
    print(type(e))
else:
    print(number)