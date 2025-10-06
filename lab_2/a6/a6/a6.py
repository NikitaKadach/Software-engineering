
N = int(input())
hours = N // 3600 % 24
minutes = N % 3600 // 60
seconds = N % 60
print("{}:{:02d}:{:02d}".format(hours, minutes, seconds))
