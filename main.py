import math

n = int(input("Введите количество точек"))
dots = []

for i in range(n):
    x = float(input("Введите х"))
    y = float(input("Введите y"))
    dots.append([x, y])

q, w, e, r, t, u, a, b, s = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
n, i = 0, 0

for i in range(n):
    q += n * dots[i][0] * dots[i][1]
    w += dots[i][0]

for i in range(n):
    e += dots[i][1]
    r = q - w * e

for i in range(n):
    t += n * math.pow(dots[i][0], 2)

for i in range(n):
    u += dots[i][0]
    u = math.pow(u, 2)

for i in range(n):
    a = r / (t - u)

for i in range(n):
    b = 1 / n * (e - a * w)

for i in range(n):
    s += math.pow(dots[i][1] - (a * dots[i][0] + b), 2)

print(a)
print(b)
print(s)
