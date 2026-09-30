import numpy as np
import matplotlib.pyplot as plt

# establecer 200 puntos entre 0 y 2 pi, una vuelta completa
x = np.linspace(0, 2 * np.pi, 200)

plt.plot(x, np.sin(x))
plt.title("sen(x) - taller de Python")
plt.show()