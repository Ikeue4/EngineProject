# Industrial Design - Engine Project

[Click here to download the most recent release](https://github.com/Ikeue4/EngineProject/tree/main/Code)

[Please read the install instructions below](#Installation-Instructions)

## Example
![[Alt text](https://github.com/Ikeue4/EngineProject/blob/main/Examples/Screenshot%202024-04-01%20204237.PNG?raw=true)

## Indtroduction

Welcome to my Engine Project, this project is free for all, however, I did not make all of this!
This project combines lots of other people working, including my own, the main idea for the engine is from Tom Stanton.
His videos were a starting point [click here](https://www.youtube.com/watch?v=FoQUwpfFnnE) his model is what the simulated engine is modelled after.
So if you want to learn more about how he made it go, check him out!

However, his videos were a good starting point, here I wanted to dive deeper into how the engine works, and the important questions so I could simulate it to a degree.
I will go further into detail about how this was achieved later. I also want to say thanks to my engineering teacher and math teacher for help in their respective areas they were a great help.

In the future, I want to further improve the detail of the sim, although this will take a lot of effort. When running the sim currently you might run into some performance issues as the sim tries to run in real-time on a single core, which can lead to different levels of success depending on your system. My short-term solution to this is to run the sim and then save the different frames to a gif, I am aware that this is not a good way of doing things at it takes a long time. Instead, I want to implement a rendering feature as currently, the user can't change anything once the sim is going we can pre-render what we need. I am looking into other solutions like writing the code in c++ but in the short term, it will stay as a simple sim. 

I do want to make the project like the [Engine Simulator](https://github.com/Engine-Simulator/engine-sim-community-edition) where you can control things on the fly. But as I said earlier in its current form this is not possible.

I do enjoy working on this project and I hope to put out a few more big revisions before I decide what way I should take the project.

## Installation Instructions

For now, it is pretty straightforward forward just go to the download link for the sim get the Python file and download the dependencies. [file](https://github.com/Ikeue4/EngineProject/tree/main/Code)

## Code Explanation

### Libraries Imported:
- `import math`: Mathematical functions.
- `import matplotlib.pyplot as plt`: Plotting graphs.
- `import matplotlib.animation as animation`: Creating animations.
- `import numpy as np`: Numerical calculations.

### Functions Defined:
1. **`slider(origin, current, step)`**:
   - Moves a slider along the crankshaft.

2. **`slope(x1, y1, x2, y2)`**:
   - Calculates the slope of a line given its coordinates.

3. **`angle_between_lines(x1, y1, x2, y2, x3, y3, x4, y4)`**:
   - Calculates the angle between two lines formed by the given coordinates.

### Main Functions:
1. **`draw_engine(Q_x, Q_y)`**:
   - Plots various components of the engine mechanism.

2. **`animate(i, ax1, ax2, ax3, ax4, rpm_text)`**:
   - Animates each frame of the simulation.

### Variables and Constants:
- **Constants**: `pi`, `radius`, `connector_rod`, `psi`, `area_of_pisten`, `psi_per_sqr`, `cycle_count`, `MAX_DATA_POINTS`.
- **Global Variables**: `q`, `torque_values`, `angle_values`, `past_positions`, `temp_max`, `rpm_values`, `volume_values`, `psi_values`, `valve`, `psi_change`.

### Animation:
- Uses `animation.FuncAnimation()` to create an animation.
- Updates the plot for each frame and displays engine parameters.

### Plotting:
- Plots engine components and parameters like torque, angle, power, and PSI in separate subplots.

### Operation:
- Simulates engine mechanism dynamics and performance.
- Includes features like valve timing and pressure calculation.

## Physics Behind the Simulation

### 1. Engine Mechanism Dynamics:
- **Crankshaft and Piston Motion**:
  - The crankshaft converts the reciprocating motion of the piston into rotational motion.
  - The piston moves up and down within the cylinder due to the combustion process.

- **Torque Generation**:
  - Torque is generated due to the pressure exerted on the piston during the power stroke.
  - Torque causes the crankshaft to rotate, transferring power to the drivetrain.

- **Valve Timing**:
  - The timing of intake and exhaust valves affects engine performance.
  - Proper valve timing ensures efficient intake of air-fuel mixture and exhaust gas expulsion.

### 2. Mathematical Formulations Used:
- **Trigonometry**:
  - Trigonometric functions are used to calculate positions and angles of engine components.
  - The sine and cosine functions relate the linear motion of the piston to the rotational motion of the crankshaft.

- **Pressure Calculations**:
  - Pressure inside the cylinder is calculated based on the ideal gas law.
  - Pressure affects the force exerted on the piston, thus influencing torque generation.

- **Angular Velocity and RPM**:
  - Angular velocity is the rate of change of angular displacement.
  - RPM (revolutions per minute) is calculated based on angular velocity to measure engine speed.

### 3. Thermodynamics:
- **Ideal Gas Law**:
  - The pressure of the gas inside the cylinder is calculated using the ideal gas law: \( PV = nRT \).
  - This law relates pressure (\(P\)), volume (\(V\)), temperature (\(T\)), and the number of moles (\(n\)) of the gas.

- **Combustion Process**:
  - The simulation accounts for the combustion process, where fuel is ignited to produce high-pressure gases.
  - This high-pressure gas exerts force on the piston, contributing to torque generation.

### 4. Fluid Dynamics:
- **Air-Fuel Mixture**:
  - The simulation considers the dynamics of the air-fuel mixture entering the combustion chamber.
  - Proper mixing and combustion of the air-fuel mixture are essential for engine efficiency.

### 5. Mechanical Engineering Principles:
- **Force and Motion**:
  - Newton's laws of motion govern the movement of engine components.
  - Force exerted by the combustion gases on the piston results in mechanical work and motion.

- **Energy Conversion**:
  - The simulation demonstrates the conversion of chemical energy (from fuel) into mechanical energy (torque and power).

By incorporating these physical principles and mathematical formulations, the simulation provides insights into the dynamic behavior and performance of the engine mechanism.

