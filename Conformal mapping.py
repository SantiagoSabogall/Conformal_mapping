import numpy as np
import matplotlib.pyplot as plt

def conformal_map(z):
    return  - 1 / z**2    #Define the complex function

# Define the points of the region to be transformed(Straight line)

points = np.array([i + 6j for i in np.linspace(-100, 100, 1000)]) 

# Points of the region to be transformed(circular region)

""""
theta = np.linspace(0, 2*np.pi, 1000)
radius = 5
points = radius * np.exp(1j * theta)   #Complex function in its exponential form(r*e^{iθ})
"""

mapped_points = conformal_map(points)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))


ax[0].plot(points.real,points.imag, 'bo-')
ax[0].set_title('z-plane')
ax[0].autoscale()
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].grid(True)

    
ax[1].plot(mapped_points.real, mapped_points.imag, 'ro-')
ax[1].set_title('w-plane')
ax[1].autoscale()
ax[1].set_xlabel('u')
ax[1].set_ylabel('v')
ax[1].grid(True)

plt.show()
