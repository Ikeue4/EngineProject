import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

PSIMin = 1
PSIMax = 50

fig, ax = plt.subplots()  # Create a figure containing a single axes.

def CalculateFoce(Min,Max):
    WidthOfPistonInM = 0.015
    LengthOfPistonInM = 0.015
    Output = []
    OutputY = []
    OutputX = []
    
    for point in range(Min,Max):
        Pascals = point*6894.75729
        
        AreaOfPiston = WidthOfPistonInM*LengthOfPistonInM
        
        OutputY.append(Pascals*AreaOfPiston)
        OutputX.append(point)
        
        
    return OutputX,OutputY


data1,data2 = CalculateFoce(PSIMin,PSIMax)
ax.grid()
ax.set_title('Relation Between Psi and Pascals')
ax.set_xlabel('Pressure (Psi)')
ax.set_ylabel('Force N/m^2')
ax.scatter(data1, data2, s=50, facecolor='C0', edgecolor='k')
plt.show()

