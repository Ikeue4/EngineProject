import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
frames_list = []

def slider(origin, current, step):
    """
    Moves the slider along the crankshaft.
    """
    if current <= origin:
        current += step
    else:
        current = -origin
    return current

def slope(x1, y1, x2, y2):
    """
    Calculate the slope of a line given its coordinates.
    """
    if x2 - x1 == 0:
        return float('inf')  # vertical line, return infinity
    else:
        return (y2 - y1) / (x2 - x1)

def angle_between_lines(x1, y1, x2, y2, x3, y3, x4, y4):
    # Calculate direction vectors for each line
    v1 = (x2 - x1, y2 - y1)
    v2 = (x4 - x3, y4 - y3)
    # Normalize the vectors
    v1_norm = v1 / np.linalg.norm(v1)
    v2_norm = v2 / np.linalg.norm(v2)
    # Calculate the dot product
    dot_product = np.dot(v1_norm, v2_norm)
    # Calculate the angle in radians
    angle = np.arccos(dot_product)
    return angle

def draw_engine(Q_x,Q_y):
    #Ploting other important stuff that stays the same
    ax1.plot([0, 0],[0+radius+connector_rod*0.35, connector_rod+radius], color='red', alpha=0.5)
    ax1.plot([3,Q_y],[Q_x,Q_x], color='black')
    ax1.plot([-3,Q_y],[Q_x,Q_x], color='black')
    ax1.plot([-3,-3],[0+radius+connector_rod*0.3,connector_rod*1.1+radius], color='black')
    ax1.plot([3,3],[0+radius+connector_rod*0.3,connector_rod*1.1+radius], color='black')
    ax1.scatter(x=0,y=0, s=radius*4000, facecolor='none', edgecolor='black', alpha=1)
    ax1.scatter(x=0,y=0, s=radius*1000, facecolor='none', edgecolor='blue', alpha=0.5)
    s = 2
    ax1.plot([0,-radius*s],[-radius*s,-radius*s], color='black')
    ax1.plot([0,radius*s],[-radius*s,-radius*s], color='black')
    ax1.plot([radius*s,radius*s],[-radius*s,0], color='black')
    ax1.plot([-radius*s,-radius*s],[-radius*s,0], color='black')
    ax1.scatter(x=0,y=0, s=50, color='purple')

def animate(i, ax1, ax2, ax3, ax4, rpm_text):
    global q, torque_values, angle_values, past_positions, temp_max, cycle_count, torque_values, angle_values, power_values, rpm_values, area_of_pisten, valve, psi_change, volume_values, psi_values
    # Calculate positions
    E_x, E_y = radius * np.cos(q), radius * np.sin(q)
    a = np.sqrt(connector_rod ** 2 - (radius * np.sin(q)) ** 2)
    Q_x, Q_y = radius * np.cos(q) + a, 0

    # Add current position to past positions list
    past_positions.append((E_x, E_y, Q_x, Q_y))

    # Limit the number of past positions stored
    past_positions = past_positions[-MAX_DATA_POINTS:]

    # Plotting
    ax1.clear()

    # Plot the past iterations
    for pos in past_positions[-10:]:
        ax1.plot([pos[1], pos[3]], [pos[0], pos[2]], color='gray', alpha=0.5)

    # Plot the current iteration
    ax1.scatter([E_y, Q_y], [E_x, Q_x], s=50, facecolor='none', edgecolor=['blue', 'red'])
    ax1.plot([E_y, Q_y], [E_x, Q_x], color='black')

    # Set fixed limits for ax1
    ax1.set_xlim(-radius - connector_rod*0.8, radius + connector_rod*0.8)
    ax1.set_ylim(-radius - connector_rod*1.5, radius + connector_rod*1.5)

    ax1.set_xlim(-20, 20)
    ax1.set_ylim(-10, 20)

    # Pressure calculations
    max_hieght = (connector_rod*1.1+radius) - (radius+connector_rod*0.35)
    volume = ((connector_rod*1.1+radius) - Q_x) * 36

    # Calculate angle for every iteration
    theta = angle_between_lines(0, 0, 0, 5, Q_x, Q_y, E_x, E_y)
    angle_values.append(math.degrees(theta))

    #simulate the timming pin
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

    if valve == False:
        p1,v1 = volume_values[0]
        psi_change = (p1*v1)/volume

    volume_values.insert(0,(volume,psi_change))
    psi_values.append(psi_change)

    force = psi * psi_per_sqr * area_of_pisten

    # Calculate torque only when piston is moving downwards
    if Q_y < E_y:
        torque = force * radius * np.cos(theta)
        torque_values.append(torque)
    else:
        torque_values.append(0)
        torque = 0

    # Calculate angular velocity
    omega = 1.1  # Example angular velocity, you need to calculate based on time/distance
    power = torque * omega
    power_values.append(power)

    # Calculate RPM
    rpm = abs(omega) * 60 / (2 * math.pi)
    rpm_values.append(rpm)

    # Limit the number of data points stored for torque, angle, power, and rpm
    torque_values = torque_values[-MAX_DATA_POINTS:]
    angle_values = angle_values[-MAX_DATA_POINTS:]
    power_values = power_values[-MAX_DATA_POINTS:]
    rpm_values = rpm_values[-MAX_DATA_POINTS:]
    psi_values = psi_values[-MAX_DATA_POINTS:]

    # Update angle for next iteration
    q = slider(pi, q, 0.1)

    # Plot torque values
    ax2.clear()
    ax2.plot(range(len(torque_values)), torque_values, marker='o', linestyle='-', color='blue')
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel('Torque')
    ax2.set_title('Torque vs. Iteration')

    # Plot angle values
    ax3.clear()
    ax3.plot(range(len(angle_values)), angle_values, marker='o', linestyle='-', color='red')
    ax3.set_xlabel('Iteration')
    ax3.set_ylabel('Angle (degrees)')
    ax3.set_title('Angle vs. Iteration')

    # Plot power values    
    ax4.clear()
    ax4.plot(range(len(angle_values)), psi_values, marker='o', linestyle='-', color='green')
    ax4.set_xlabel('Iteration')
    ax4.set_ylabel('Power')
    ax4.set_title('PSI vs. Iteration')

    # Add RPM text on the first graph
    ax1.text(13, 11, f'RPM: {rpm:.2f}')
    ax1.text(4,Q_x, f'volume:{volume:.2f}')
    ax1.text(13,13, f'degrees:{math.degrees(theta):.2f}')
    ax1.text(13,12, f'valve = {valve}')
    ax1.text(13,10, f'Possiton:{(connector_rod*1.1+radius) - Q_x:.2f}')
    ax1.text(13,9, f'PSI:{psi_change:.2f}')

    #Ploting other important stuff that stays the same
    draw_engine(Q_x, Q_y)
    if valve == True:
        color = 'green'
    else:
        color = 'red'
    ax1.scatter(x=0,y=17.4, color=color)
    ax1.text(-15,-9, 'version: 0.1')

# Set up plots
fig = plt.figure(figsize=(18, 18))
fig.set_facecolor('grey')

# Subplot grid configuration
ax1 = plt.subplot2grid((2, 2), (0, 0))
ax2 = plt.subplot2grid((2, 2), (1, 0))
ax3 = plt.subplot2grid((2, 2), (1, 1))
ax4 = plt.subplot2grid((2, 2), (0, 1))

ax1.set_aspect('equal')

torque_values = []
angle_values = []
power_values = []
past_positions = []
rpm_values = []
volume_values = []
psi_values = []

# Constants and initial conditions
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
temp_max = []
cycle_count = 3  # Number of cycles you want to plot
MAX_DATA_POINTS = 100

ani = animation.FuncAnimation(fig, animate, fargs=(ax1, ax2, ax3, ax4, rpm_values), frames=frames, interval=100)
plt.show()
