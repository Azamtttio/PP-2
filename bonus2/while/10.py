max = 0
index = -1
a = -1
len = 0
while a != 0:
    a = int(input())
    if a > max:
        max = a
        index = len
    len += 1
print(index)