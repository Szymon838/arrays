import numpy as np
import matplotlib.pyplot as plt

x_deg = np.linspace(0, 360, 1000)  

x_rad = np.radians(x_deg)

y = np.sin(x_rad)

plt.plot(x_deg, y, label=r"$y = \sin(x)$")

plt.title("Graph of y = sin(x)")
plt.xlabel("x (degrees)")
plt.ylabel("y")

plt.grid(True)
plt.legend()

plt.show()