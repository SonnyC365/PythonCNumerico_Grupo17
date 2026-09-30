import numpy as np
import matplotlib.pyplot as plt

# establecer 200 puntos entre 0 y 2 pi, una vuelta completa
x = np.linspace(0, 2 * np.pi, 200)
seno = np.sin(x)
coseno = np.cos(x)

# figure numero 1 - seno
plt.figure(1)
plt.plot(x, seno, label="sen(x)")

# figure numero 2 - coseno
plt.figure(2)
plt.plot(x, coseno, label="cos(x)")

plt.title("grafica del seno")

plt.plot(x, seno + coseno, "g--", label="sen(x) + cos(x)")

plt.legend()

plt.show()