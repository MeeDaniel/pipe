
import numpy as np                       # Создаём массивы чисел
import matplotlib.pyplot as plt          # Библиотека для графиков
from scipy.integrate import solve_ivp    # Решатель задач с начальными условиями

def system(t, y):                        # Описываем нашу систему уравнений
    x = y[0]                             # Первый элемент: положение груза
    v = y[1]                             # Второй элемент: скорость груза
    return [v, -5*v - 500*x - 10000*x**3]  # Возвращаем x' и v'

t = np.linspace(0, 5, 500)               # 500 точек от 0 до 5 секунд
solution = solve_ivp(system, [0, 5], [0.02, 0], t_eval=t)  # Решаем задачу
print(solution.success)                  # Проверяем, успешно ли найдено решение

plt.plot(solution.t, solution.y[0])      # Рисуем график положения груза
plt.xlabel('Time (s)')                   # Подпись оси X
plt.ylabel('Displacement (m)')           # Подпись оси Y
plt.title('Task 3: Spring and damper')   # Заголовок графика
plt.grid()                               # Включаем сетку
plt.savefig('task3_case23.png')          # Сохраняем график в файл
plt.show()                               # Показываем график
