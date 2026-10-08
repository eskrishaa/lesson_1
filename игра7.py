
# ============================================================
# ИГРА «КОЛОДЕЦ У СТАРОЙ МЕЛЬНИЦЫ»
# Автор: Воробьева Ирина
# Дата: сентябрь 2026
#
# Пункт 4 — «заглянуть в колодец».
# Пункт 5 — «зачерпнуть воды».
# Пункт 6 — «тренировка».
# Пункт 7 — «искать врага».
# Пункт 0 — выход из подземелья.
# ============================================================

import random

# --- Заголовок ---

title = "КОЛОДЕЦ У СТАРОЙ МЕЛЬНИЦЫ"
frame = "=" * 32

print(frame)
print(" " + title + " ")
print(frame)

print()

# --- Знакомство с героем ---

print("Как зовут героя?")
hero_name = input()

print(f"Добро пожаловать, {hero_name}!")
print("Ты подходишь к колодцу у старой мельницы. Крыша провалилась, сруб почернел, из глубины тянет холодом.")

print()

# --- Настройка героя ---

print("Настройка героя.")
print("Здоровье, сила, ловкость, удача – по одному числу в строке:")

while True:
    try:
        health = int(input())
        strength = int(input())
        agility = int(input())
        luck = int(input())

        if health <= 0:
            raise ValueError(f"Здоровье должно быть положительным, вы ввели {health}")
        if strength < 0 or agility < 0 or luck < 0:
            raise ValueError("Характеристики не могут быть отрицательными")

        break
    except ValueError as e:
        print(f"{e}. Введите все четыре снова:")

# --- Расчёт урона ---

base_attack = 10

damage = base_attack + strength * 1.5
crit_damage = damage * 2

stamina = agility + luck // 2

# --- Формуляр героя ---

print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Удача: {luck}")

print()

print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Запас сил: {stamina}")

print()

# --- Обитатели подземелья ---

enemies = [
    "пещерный паук",
    "слепой нетопырь",
    "болотная пиявка",
]

# --- Главный цикл игры ---

running = True
actions = 0
menu_last = 7
outcome = "прерывание"

try:
    while running:
        print("Что делаешь?")
        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - заглянуть в колодец")
        print("5 - зачерпнуть воды")
        print("6 - тренировка")
        print("7 - искать врага")
        print("0 - выйти из подземелья")

        print()

        while True:
            choice = input()
            try:
                menu_number = int(choice)
            except ValueError:
                print("Такого пункта нет. Введи номер пункта из меню.")
                continue
            if 0 <= menu_number <= menu_last:
                break
            print("Такого пункта нет. Введи номер пункта из меню.")

        match choice:
            case "1":
                print("Вы осмотрелись. Сруб колодца оброс мхом, на дне блестит вода.")

            case "2":
                cost = 2
                if stamina >= cost:
                    stamina -= cost
                    print("Вы осторожно идёте вперёд. Доски настила скрипят под ногами.")
                else:
                    health -= cost - stamina
                    stamina = 0
                    print("Сил больше нет — вы идёте на одном упорстве.")

            case "3":
                stamina += 3
                print("Вы присели отдохнуть у сруба. Силы понемногу возвращаются.")

            case "4":
                print("Вы заглядываете в колодец. В темноте ничего не видно, только холод тянет снизу.")

            case "5":
                stamina += 1
                print("Вы зачерпнули воды и умылись. Свежесть придаёт сил.")

            case "6":
                strikes = 6
                total_damage = 0
                crit_count = 0

                print("Вы подходите к старому столбу у колодца.")
                print("Он стоит здесь с тех пор, как мельница ещё работала.")

                print()
                print(f"Наносите {strikes} ударов.")

                for i in range(1, strikes + 1):
                    if i % 3 == 0:
                        hit_damage = crit_damage
                        crit_count += 1
                        print(f"Удар {i}: {hit_damage:.1f} – критический!")
                    else:
                        hit_damage = damage
                        print(f"Удар {i}: {hit_damage:.1f}")

                    total_damage += hit_damage

                print()
                print(f"Итог: {strikes} ударов, критических ударов: {crit_count}")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {total_damage / strikes:.1f}")

                stamina -= 3

            case "7":
                enemy = random.choice(enemies)
                enemy_health = random.randint(15, 25)
                enemy_damage = random.randint(2, 5)

                print(f"Из темноты выползает {enemy}!")
                print(f"Здоровье врага: {enemy_health}")

                while enemy_health > 0 and health > 0:
                    hit = damage + random.randint(-3, 3)
                    enemy_health -= hit
                    print(f"Вы бьёте: {hit:.1f} урона. У врага осталось {enemy_health:.1f}")

                    if enemy_health <= 0:
                        print(f"{enemy} повержен!")
                        break

                    back = enemy_damage + random.randint(-1, 1)
                    health -= back
                    print(f"{enemy} бьёт в ответ: {back} урона. У вас осталось {health} здоровья")

                if health <= 0:
                    print("Вы падаете...")

            case "0":
                print("Вы поднимаетесь обратно к свету. Подземелье остаётся позади.")
                outcome = "выход"
                running = False

            case _:
                # недостижимо: неверный ввод отсекается до match
                print("Такого действия нет.")

        if health <= 0:
            print(f"{hero_name} падает без сил. Подземелье забирает ещё одного искателя.")
            outcome = "гибель"
            running = False

        if running:
            actions += 1

        print()
        print(f"Здоровье: {health:5d}   Запас сил: {stamina:5d}")

except KeyboardInterrupt:
    print()
    print("Игрок прервал сеанс.")

finally:
    print()
    print(frame)
    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Сеанс прерван, {hero_name}. Действий совершено: {actions}.")
    print(frame)
