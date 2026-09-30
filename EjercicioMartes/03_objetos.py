import numpy as np
import matplotlib.pyplot as plt

# establecer 200 puntos entre 0 y 2 pi, una vuelta completa
x = np.linspace(0, 2 * np.pi, 200)
seno = np.sin(x)
coseno = np.cos(x)

fig, (ax_seno, ax_coseno) = plt.subplots(1, 2, figsize=(12, 5))

# axe numero 1 - seno y suma de seno mas coseno
ax_seno.plot(x, seno, label="sen(x)")
ax_seno.plot(x, seno + coseno, "g--", label="sen(x) + cos(x)")
ax_seno.set_title("Gráfica del seno")
ax_seno.legend()

# axe numero 2 - coseno
ax_coseno.plot(x, coseno, color="tab:orange", label="cos(x)")
ax_coseno.set_title("gráfica del coseno")
ax_coseno.legend()

fig.tight_layout()
fig.savefig("panel_taller.png", dpi=300, bbox_inches="tight")
plt.show()
