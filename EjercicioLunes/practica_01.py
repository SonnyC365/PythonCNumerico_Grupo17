# PRACTICA 1

# PASO 1. Importar la libreria Numpy

import numpy as np

# PASO 2. Agregar nuestras variables

velocidad = 5

tiempos = np.array([0, 1, 2, 3, 4, 5])

# PASO 3. Calcular la distancia recorrida

distancia = velocidad * tiempos

print("Distancia máxima:", np.max(distancia))

print("Distancia promedio:", np.mean(distancia))

print("Distancia mínima:", np.min(distancia))
