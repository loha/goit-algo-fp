import matplotlib.pyplot as plt
import numpy as np

def draw_pythagoras_tree(ax, x, y, angle, length, level):
    if level == 0:
        return
    
    # Вираховуємо координати нової вершини
    x_new = x + length * np.cos(angle)
    y_new = y + length * np.sin(angle)
    
    # Малюємо лінію для поточної гілки
    ax.plot([x, x_new], [y, y_new], color="green", lw=2 * level)

    # Малюємо праву і ліву гілки рекурсивно
    draw_pythagoras_tree(ax, x_new, y_new, angle - np.pi/4, length * np.cos(np.pi/4), level - 1)
    draw_pythagoras_tree(ax, x_new, y_new, angle + np.pi/4, length * np.cos(np.pi/4), level - 1)

# Налаштування графіку
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

# Користувач вводить рівень рекурсії
level = int(input("Введіть рівень рекурсії (наприклад, 5): "))

# Початкова точка та параметри
start_x = 0
start_y = 0
start_angle = np.pi / 2  # Вказуємо вгору (90 градусів)
start_length = 100

# Починаємо малювання
draw_pythagoras_tree(ax, start_x, start_y, start_angle, start_length, level)

# Відображення фракталу
plt.show()