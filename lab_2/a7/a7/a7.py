x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
scolor = (x1 + y1) % 2 == (x2 + y2) % 2
result = ["NO", "YES"]
print(result[scolor])
if scolor:
    color = "White" if (x1 + y1) % 2 == 0 else "Black"
    print(color)
