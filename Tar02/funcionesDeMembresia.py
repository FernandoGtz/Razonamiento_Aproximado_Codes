# Plantilla en donde se utilizan dos bibliotecas
# para generar los datos del Universo de Discurso,
# calcular una función de membresía y graficarla
# utilizando títulos y sub ventanas.
# Virgilio LM - Jun-2025

import numpy as np
import matplotlib.pyplot as plt

# Definición de la función de membresía campana generalizada
def gbell_mf(x, a, b, c):
    return 1 / (1 + np.abs((x - c) / a) ** (2 * b))

# Datos
x = np.arange(0, 101)
mf = gbell_mf(x, a=20, b=4, c=50)

# Gráfica
plt.subplot(1, 2, 1)
plt.plot(x, mf)
plt.ylim(0, 1.2)
plt.ylabel('Grados de Membresía')
plt.title('(a) Fcn. Campana generalizada')
plt.xticks([0, 20, 40, 60, 80, 100])


plt.subplot(1, 2, 2)
plt.plot(x, mf)
plt.ylim(0, 1.2)
plt.ylabel('Grados de Membresía')
plt.title('(a) Fcn. Campana generalizada')
plt.xticks([0, 20, 40, 60, 80, 100])

plt.tight_layout()
plt.show()