def euler(f, x0, y0, h, n):
    x = x0
    y = y0
    xs = [x0]
    ys = [y0]
    for i in range(n):
        y = y + h * f(x, y)
        x = x + h
        xs.append(x)
        ys.append(y)
    return xs, ys

# Exemplo de uso:
def f(x, y):
    return y

x0 = 0
y0 = 1
h = 0.1
n = 10

xs, ys = euler(f, x0, y0, h, n)
print(xs)
print(ys)
