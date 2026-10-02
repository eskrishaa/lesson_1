# ============================================================
# ИГРА «КОЛОДЕЦ У СТАРОЙ МЕЛЬНИЦЫ»
# Автор: Воробьева Ирина
# Дата: сентябрь 2026
#
# Пункт 4 — «заглянуть в колодец»: герой
# наклоняется над срубом и всматривается
# в тёмную воду.
#
# Пункт 5 — «зачерпнуть воды»: герой зачерпывает
# воды из колодца и умывается, восстанавливая силы.
#
# Пункт 6 — «тренировка»: герой наносит серию
# ударов по старому столбу у колодца.
#
# Пункт 0 — выход из подземелья.
# ============================================================

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

health = int(input())
strength = int(input())
agility = int(input())
luck = int(input())

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

# --- Главный цикл игры ---

running = True
actions = 0

while running:
    print("Что делаешь?")
    print("1 - осмотреться")
    print("2 - идти вперёд")
    print("3 - отдохнуть")
    print("4 - заглянуть в колодец")
    print("5 - зачерпнуть воды")
    print("6 - тренировка")
    print("0 - выйти из подземелья")

    print()

    valid = ("0", "1", "2", "3", "4", "5", "6")
    choice = input()

    while choice not in valid:
        print("Такого пункта нет. Введи номер пункта из меню.")
        choice = input()

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

        case "0":
            print("Вы поднимаетесь обратно к свету. Подземелье остаётся позади.")
            running = False

        case _:
            print("Такого действия нет.")

    if health <= 0:
        print(f"{hero_name} падает без сил. Подземелье забирает ещё одного искателя.")
        running = False

    if running:
        actions += 1

    print()
    print(f"Здоровье: {health:5d}   Запас сил: {stamina:5d}")

# --- Прощание ---

print()
print(frame)
if health <= 0:
    print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
else:
    print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
print(frame)
