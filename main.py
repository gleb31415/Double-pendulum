import numpy as np
import tkinter as tk
import colorsys

# Constants
g, l1, l2 = -9.81, 1.0, 1.0
m1, m2 = 1.0, 1.0
num_pendulums = 400
t_step = 0.005
diff = 0.000001
wd = int(2)

initial_conditions = np.array([
    [np.pi / 2 + i * diff, 0, np.pi / 4 + i * diff, 0]
    for i in range(num_pendulums)
], dtype=float)


def derivatives(y):
    theta1 = y[:, 0]
    z1 = y[:, 1]
    theta2 = y[:, 2]
    z2 = y[:, 3]
    delta_theta = theta1 - theta2

    sin_delta = np.sin(delta_theta)
    cos_delta = np.cos(delta_theta)

    dnm1 = l1 * (m1 + m2 * sin_delta ** 2)
    dnm2 = l2 * (m1 + m2 * sin_delta ** 2)

    dz1dt = (
                    m2 * g * np.sin(theta2) * cos_delta -
                    m2 * sin_delta * (l1 * z1 ** 2 * cos_delta + l2 * z2 ** 2) -
                    (m1 + m2) * g * np.sin(theta1)
            ) / dnm1

    dz2dt = (
                    (m1 + m2) * (l1 * z1 ** 2 * sin_delta - g * np.sin(theta2) +
                                 g * np.sin(theta1) * cos_delta) +
                    m2 * l2 * z2 ** 2 * sin_delta * cos_delta
            ) / dnm2

    dtheta1dt = z1
    dtheta2dt = z2

    return np.stack([dtheta1dt, dz1dt, dtheta2dt, dz2dt], axis=1)


# Initialize Tkinter
root = tk.Tk()
root.title("Multiple Pendulums with Rainbow Gradient")
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

scale, offset_x, offset_y = 150, 300, 300


def get_rainbow_color(i, max_value):
    hue = i / max_value
    r, g_col, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    return f'#{int(r * 255):02x}{int(g_col * 255):02x}{int(b * 255):02x}'


colors = [get_rainbow_color(i, num_pendulums) for i in range(num_pendulums)]
rods1 = [canvas.create_line(0, 0, 0, 0, width=wd, fill=colors[i]) for i in range(num_pendulums)]
rods2 = [canvas.create_line(0, 0, 0, 0, width=wd, fill=colors[i]) for i in range(num_pendulums)]


def update_pendulums():
    global initial_conditions
    dy = derivatives(initial_conditions)
    initial_conditions += dy * t_step

    theta1 = initial_conditions[:, 0]
    theta2 = initial_conditions[:, 2]

    x1 = l1 * np.sin(theta1)
    y1 = l1 * np.cos(theta1)
    x2 = x1 + l2 * np.sin(theta2)
    y2 = y1 + l2 * np.cos(theta2)

    x1_screen = x1 * scale + offset_x
    y1_screen = offset_y - y1 * scale
    x2_screen = x2 * scale + offset_x
    y2_screen = offset_y - y2 * scale

    for j in range(num_pendulums):
        canvas.coords(rods1[j], offset_x, offset_y, x1_screen[j], y1_screen[j])
        canvas.coords(rods2[j], x1_screen[j], y1_screen[j], x2_screen[j], y2_screen[j])

    root.after(10, update_pendulums)


update_pendulums()
root.mainloop()
