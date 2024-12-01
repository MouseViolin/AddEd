import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def surface(x, y, e):
    a = 2
    if e < 1:  # Эллипс
        b = a * np.sqrt(1 - e**2)
    elif e == 1:  # Парабола
        b = a
    else:  # Гипербола
        b = a * np.sqrt(e**2 - 1)

    if e < 1:
        z = x**2 / a**2 + y**2 / b**2 - 1  # Эллипс
    elif e == 1:
        z = y**2 - x**2  # Парабола
    else:
        z = x**2 / a**2 - y**2 / b**2 - 1  # Гипербола
    return z


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")


x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)


ax.set_title("График функции с анимацией эксцентриситета")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")


# Функция для обновления графика на каждом кадре
def update(t):
    ax.cla()
    e = t
    Z = surface(X, Y, e)  # Вычисляем новые значения Z с учетом эксцентриситета
    ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none")
    ax.set_title(f"Эксцентриситет: e = {e:.2f}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_zlim(-2, 2)
    return []


ani = FuncAnimation(fig, update, frames=np.linspace(0, 2, 100), interval=500)
plt.show()
