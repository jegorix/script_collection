'''
### Документация программы

Программа использует SymPy для вычисления производных и построения графиков функций:
- Определяет f(x) = x^3 + 2x^2 + 3x + 5, вычисляет f'(x), выводит значение в x = 1.
- Строит графики f(x) (синий) и f'(x) (красный) на x от -2 до 2.
- Дополнительно: g(x) = e^x * sin(x), вычисляет g'(x).

### Требования
- SymPy: pip install sympy
- Matplotlib: pip install matplotlib

### Использование
Запустите код в Python (например, PyCharm). Вывод:
- Формулы: f(x), f'(x), f'(1), g(x), g'(x).
- График f(x) и f'(x).
'''
from sympy import symbols, diff, exp, sin
from sympy.plotting import plot
import matplotlib.pyplot as plt

x = symbols('x')
pi = 3.14

f = x**3 + 2*x**2 + 3*x + 5
# f = sin(x)

df = diff(f, x)

print(f"f(x) = {f}")
print(f"f'(x) = {df}")

x_val = 1
df_at_x = df.subs(x, x_val)
print(f"f'({x_val}) = {df_at_x}")


p1 = plot(f, (x, -2 * pi, 2 * pi), line_color='blue', label='f(x)', show=False)
p2 = plot(df, (x, -2 * pi, 2 * pi), line_color='red', label='f\'(x)', show=False)
p1.extend(p2)
p1.legend = True
p1.show()

g = exp(x) * sin(x)
dg = diff(g, x)
print(f"g(x) = {g}")
print(f"g'(x) = {dg}")


plt.show()