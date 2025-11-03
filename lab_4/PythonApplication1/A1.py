import random
import time
n = int(input("Примеров: "))
right = 0
time_all = 0
for i in range(n):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    start = time.time()
    ans = int(input(str(a) + "*" + str(b) + "="))
    t = round(time.time() - start, 1)
    if ans == a * b:
        print("Да!", t, "сек")
        right += 1
    else:
        print("Нет!", t, "сек")
    time_all += t
print("")
print("Время:", time_all, "сек")
print("Правильно:", str(right) + "/" + str(n))
print("Среднее:", time_all/n, "сек")
print("Процент:", str(round(right/n*100)) + "%")
