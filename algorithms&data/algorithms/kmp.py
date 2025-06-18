#Knuth-Morris-Pratt algorithm

t = "лилила"
a = "лилилось лилилась"
p = [0] * len(t)

i = 1
j = 0

while i < len(t):
    if t[i] == t[j]:
        p[i] = j+1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]
        

m = len(t)
n = len(a)

i = 0
j = 0

while i < n:
    if a[i] == t[j]:
        i += 1
        j += 1
        if j == m:
            print(f"подстрока найдена, позиция: от {i - m + 1} до {i}")
            break
    else:
        if j > 0:
            j = p[j-1]
        else:
            i += 1

if i == n:
    print("подстрока не найдена")