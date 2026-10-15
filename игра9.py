# ============================================================
# ИГРА «КОЛОДЕЦ У СТАРОЙ МЕЛЬНИЦЫ»
# Автор: Воробьева Ирина
# Дата: сентябрь 2026
#
# Пункт 4 — «заглянуть в колодец».
# Пункт 5 — «зачерпнуть воды».
# Пункт 6 — «тренировка».
# Пункт 7 — «искать врага».
# Пункт 8 — «таблица лидеров».
# Пункт 0 — выход из подземелья.
#
# Журнал боя — список списков [номер раунда, урон героя, урон врага].
# Если враг бил одинаково сильно дважды, max вернёт первую такую
# строку — это устойчивость сортировки Python (Timsort), не случайность.
# ============================================================

import random

# --- Константы игры ---

title = "КОЛОДЕЦ У СТАРОЙ МЕЛЬНИЦЫ"
frame = "=" * 32

base_attack = 10
enemies = [
    "пещерный паук",
    "слепой нетопырь",
    "болотная пиявка",
]

log = []

# --- Функции ---


def hero_hit(strike_n):
    """Урон героя в удар номер strike_n.
    Возвращает пару (hit, crit): урон и признак критического удара.
    Читает глобальные damage и crit_damage, не меняет ничего.
    """
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False


def fight(enemy, hero_health):
    """Бой с enemy до гибели одного из двоих.
    Печатает строки раундов. Возвращает (rounds, won, hero_health):
    таблицу раундов, признак победы героя и здоровье после боя.
    Глобальные переменные не меняет: здоровье приходит параметром
    и возвращается новым значением.
    """
    enemy_hp = 45.0
    rounds = []
    round_n = 0

    print(f"Из темноты выползает {enemy}! Здоровье врага: {enemy_hp}")

    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n)
        enemy_hp -= hit

        line = f"Раунд {round_n}: герой наносит {hit:.1f}"
        if crit:
            line += " – критический!"

        if enemy_hp <= 0:
            line += " Враг падает."
            rounds.append([round_n, hit, 0])
        else:
            blow = random.randint(2, 6)
            hero_health -= blow
            line += f" У врага осталось {enemy_hp:.1f}. {enemy.capitalize()} бьёт в ответ: {blow}."
            rounds.append([round_n, hit, blow])

        print(line)

    return rounds, enemy_hp <= 0, hero_health


def print_leaderboard(log):
    """Печатает топ-3 раундов по урону героя и рекорд врага.
    Возвращает None: контракт функции – печать, а не данные.
    """
    if not log:
        print("Вы ещё не сражались.")
        return

    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]

    print("Таблица лидеров (урон героя):")
    for i in range(len(top)):
        print(f"{i + 1}. Раунд {top[i][0]}: {top[i][1]:.1f}")

    worst = max(log, key=lambda r: r[2])
    print(f"Сильнейший удар врага: {worst[2]} (раунд {worst[0]}).")


def print_run_summary(log):
    """Печатает итог забега: суммарный и средний урон героя.
    Возвращает None. Безопасна на пустом журнале.
    """
    total = sum(r[1] for r in log)
    rounds = len(log)

    if rounds > 0:
        print(f"Урон: {total:.1f} за {rounds} раундов, в среднем {total / rounds:.1f}.")
    else:
        print("В этом забеге боёв не было.")


# --- Заголовок ---

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
menu_last = 8
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
        print("8 - таблица лидеров")
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
                    hit_damage, crit = hero_hit(i)
                    if crit:
                        crit_count += 1
                        print(f"Удар {i}: {hit_damage:.1f} – критический!")
                    else:
                        print(f"Удар {i}: {hit_damage:.1f}")
                    total_damage += hit_damage

                print()
                print(f"Итог: {strikes} ударов, критических ударов: {crit_count}")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {total_damage / strikes:.1f}")

                stamina -= 3

            case "7":
                if not enemies:
                    print("Вы спускаетесь вниз. Но подземелье пусто.")
                else:
                    enemy = random.choice(enemies)
                    rounds, won, health = fight(enemy, health)

                    for r in rounds:
                        log.append(r)

                    if won:
                        enemies.remove(enemy)
                        print(f"{enemy.capitalize()} повержен! Осталось врагов: {len(enemies)}.")

                    print(f"Бой: {len(rounds)} раундов.")

            case "8":
                print_leaderboard(log)

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

    print_run_summary(log)

    print(frame)
