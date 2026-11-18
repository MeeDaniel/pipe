
import numpy as np                         # Работа с массивами и числами
import matplotlib.pyplot as plt            # Построение графиков
from scipy.integrate import solve_bvp      # Решение краевых задач

# SUBTASK 1: y'' + x*y' + 2*y = 4*x^3

def f1(x, y):                              # Описываем дифференциальное уравнение
    return np.array([y[1], 4*x**3 - x*y[1] - 2*y[0]])  # Возвращаем y' и y''

def bc1(left, right):                      # Описываем граничные условия
    return np.array([left[0] + left[1] - 1, right[0] - 2])  # Оба условия должны дать ноль

x = np.linspace(0.5, 1, 10)                # 10 точек от 0.5 до 1
initial = np.zeros((2, len(x)))            # Начальное приближение: нули для y и y'
solution = solve_bvp(f1, bc1, x, initial)  # Ищем численное решение
x_plot = np.linspace(0.5, 1, 100)          # 100 точек для гладкого графика
plt.figure()                               # Создаём первый рисунок
plt.plot(x_plot, solution.sol(x_plot)[0], label='SciPy')  # Кривая численного решателя
plt.plot([0.5, 0.75, 1], [3.42647, 2.76654, 2], 'o--', label='Finite differences')  # Точки из тетради
plt.xlabel('x')                            # Подписываем горизонтальную ось
plt.ylabel('y')                            # Подписываем вертикальную ось
plt.title('Task 2 - Subtask 1')            # Заголовок первого графика
plt.legend()                               # Показываем названия линий
plt.grid()                                 # Включаем сетку
plt.savefig('subtask1.png')                # Сохраняем первый рисунок

# SUBTASK 2: y'' - 5*y' + 6*y = 3

def f2(x, y):                              # Описываем второе уравнение
    return np.array([y[1], 5*y[1] - 6*y[0] + 3])  # Возвращаем y' и y''

def bc2(left, right):                      # Описываем граничные условия
    return np.array([left[0], right[0]])   # y(-1) = 0 и y(1) = 0

x = np.linspace(-1, 1, 10)                 # 10 точек от -1 до 1
initial = np.zeros((2, len(x)))            # Начальное приближение для y и y'
solution = solve_bvp(f2, bc2, x, initial)  # Находим решение второй задачи
x_plot = np.linspace(-1, 1, 100)           # 100 точек для графика
y_collocation = (1 - x_plot**2) * (18/59 - 21*x_plot/59)  # Твоя формула коллокации
y_galerkin = (1 - x_plot**2) * (-135/224 - 525*x_plot/224)  # Твоя формула Галёркина
plt.figure()                               # Создаём второй рисунок
plt.plot(x_plot, solution.sol(x_plot)[0], label='SciPy')  # Решение SciPy
plt.plot(x_plot, y_collocation, label='Collocation')  # Решение методом коллокации
plt.plot(x_plot, y_galerkin, label='Galerkin')  # Решение методом Галёркина
plt.xlabel('x')                            # Подпись горизонтальной оси
plt.ylabel('y')                            # Подпись вертикальной оси
plt.title('Task 2 - Subtask 2')            # Заголовок второго графика
plt.legend()                               # Названия линий
plt.grid()                                 # Сетка
plt.savefig('subtask2.png')                # Сохраняем второй рисунок
plt.show()                                 # Показываем оба графика
