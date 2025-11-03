s = input("Введите нули и единицы: ")
if len(s) < 5:
    print("Ошибка! Минимум 5 символов")
    exit()
for char in s:
    if char != "0" and char != "1":
        print("Ошибка! Только 0 и 1")
        exit()
lose = s.count("0")
max_streak = 0
cur = 0
for char in s:
    if char == "0":
        cur += 1
        max_streak = max(max_streak, cur)
    else:
        cur = 0
loss_percent = round(lose / len(s) * 100, 1)
if loss_percent < 1:
    qu = "Отличное качество"
elif loss_percent <= 5:
    qu = "Хорошее качество"
elif loss_percent < 10:
    qu = "Удовлетворительное качество"
elif loss_percent <= 20:
    qu = "Плохое качество"
else:
    qu = "Критическое состояние сети"
print(f"Общее кол-во пакетов: {len(s)}")
print(f"Количество потерь: {lose}")
print(f"Самая длинная последовательность потерь: {max_streak}")
print(f"Процент потерь: {loss_percent}%")
print(f"Состояние сети: {qu}")
