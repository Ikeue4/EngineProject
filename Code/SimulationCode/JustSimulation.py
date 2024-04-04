import math
import numpy as np
import time

def slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return float('inf')
    else:
        return (y2 - y1) / (x2 - x1)

def angle_between_lines(x1, y1, x2, y2, x3, y3, x4, y4):
    v1 = (x2 - x1, y2 - y1)
    v2 = (x4 - x3, y4 - y3)
    v1_norm = v1 / np.linalg.norm(v1)
    v2_norm = v2 / np.linalg.norm(v2)
    dot_product = np.dot(v1_norm, v2_norm)
    angle = np.arccos(dot_product)
    return angle

def slider(origin, current, step):
    if current <= origin:
        current += step
    else:
        current = -origin
    return current

pi = math.pi
radius = 4
connector_rod = 12
q = pi
psi = 300
area_of_pisten = 36
psi_per_sqr = 6894.7572932
force = psi * psi_per_sqr * area_of_pisten
valve = False
psi_change = 0
frames = 100
last_time = time.time()
torque_values = []

for _ in range(frames):
    E_x, E_y = radius * np.cos(q), radius * np.sin(q)
    a = np.sqrt(connector_rod ** 2 - (radius * np.sin(q)) ** 2)
    Q_x, Q_y = radius * np.cos(q) + a, 0

    max_hieght = (connector_rod*1.1+radius) - (radius+connector_rod*0.35)
    volume = ((connector_rod*1.1+radius) - Q_x) * 36

    theta = angle_between_lines(0, 0, 0, 5, Q_x, Q_y, E_x, E_y)

    if math.degrees(theta) <= 90 and math.degrees(theta) >= 80:
        valve = True
        if (connector_rod*1.1+radius) - Q_x < 3:
            if psi_change <= psi:
                psi_change += psi*0.2
        else:
            if psi_change > 14.7:
                psi_change = 14.7
    else:
        valve = False

    volume_values = [(0, 0)]  # Define volume_values variable and assign a default value
    p1, v1 = volume_values[0]
    psi_change = (p1 * v1) / volume

    force = psi * psi_per_sqr * area_of_pisten

    if Q_y < E_y:
        torque = force * radius * np.cos(theta)
        torque_values.append(torque)
    else:
        torque_values.append(0)
        torque = 0

    q = slider(pi, q, 0.1)

for i, torque in enumerate(torque_values):
    print(f"Iteration {i+1}: Torque = {torque}")