x = int(input("x = "))
y = int(input("y = "))
for i in range(y):
    print("#" * x)
for i in range(y):
    print("#" * (i + 1))
for i in range(y):
    if i == 0 or i == y - 1:
        print("#" * x)
    else:

        print("#" + " " * (x - 2) + "#")
