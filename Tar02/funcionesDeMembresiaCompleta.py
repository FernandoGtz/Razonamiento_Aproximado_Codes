# Plantilla adaptada para graficar 4 funciones de membresía:
# Triangular, Trapezoidal, Gaussiana y Campana Generalizada.
# Se generan datos del Universo de Discurso y se visualizan
# utilizando una cuadrícula de 2x2.
# Adaptación basada en Virgilio LM - Jun-2025

import numpy as np
import matplotlib.pyplot as plt

# Definición de las Funciones de Membresía

def trimf(x, a, b, c):
    """Función Triangular: a (inicio), b (pico), c (fin)"""
    # Se usa max y min para crear la forma triangular vectorizada
    return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))

def trapmf(x, a, b, c, d):
    """Función Trapezoidal: a (inicio pies), b (inicio hombro), c (fin hombro), d (fin pies)"""
    # Similar a la triangular pero con un techo plano (min con 1)
    return np.maximum(0, np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)))

def gaussmf(x, mean, sigma):
    """Función Gaussiana: mean (centro), sigma (desviación estándar/ancho)"""
    return np.exp(-((x - mean) ** 2) / (2 * sigma ** 2))

def gbell_mf(x, a, b, c):
    """Función Campana Generalizada: a (ancho), b (pendiente), c (centro)"""
    return 1 / (1 + np.abs((x - c) / a) ** (2 * b))

#Datos del Universo de Discurso
x = np.arange(0, 101)

#Cálculo de los valores de membresía (Parámetros arbitrarios)

# Triangular: Inicia en 10, pico en 40, termina en 70
y_tri = trimf(x, a=10, b=40, c=70)

# Trapezoidal: Sube en 20, plano de 40 a 60, baja en 90
y_trap = trapmf(x, a=20, b=40, c=60, d=90)

# Gaussiana: Centro en 50, dispersión de 15
y_gauss = gaussmf(x, mean=50, sigma=15)

# Campana: Ancho 20, pendiente 4, centro 50
y_bell = gbell_mf(x, a=20, b=4, c=50)

#4. Gráficas
plt.figure(figsize=(10, 8)) # Tamaño de la ventana completa

# Gráfica 1: Triangular
plt.subplot(2, 2, 1)
plt.plot(x, y_tri, 'b', linewidth=2)
plt.title('(a) Fcn. Triangular')
plt.ylabel('Grados de Membresía')
plt.ylim(0, 1.1)
plt.grid(True, linestyle='--', alpha=0.6)

# Gráfica 2: Trapezoidal
plt.subplot(2, 2, 2)
plt.plot(x, y_trap, 'r', linewidth=2)
plt.title('(b) Fcn. Trapezoidal')
plt.ylim(0, 1.1)
plt.grid(True, linestyle='--', alpha=0.6)

# Gráfica 3: Gaussiana
plt.subplot(2, 2, 3)
plt.plot(x, y_gauss, 'g', linewidth=2)
plt.title('(c) Fcn. Gaussiana')
plt.ylabel('Grados de Membresía')
plt.xlabel('Universo de Discurso')
plt.ylim(0, 1.1)
plt.grid(True, linestyle='--', alpha=0.6)

# Gráfica 4: Campana Generalizada
plt.subplot(2, 2, 4)
plt.plot(x, y_bell, 'm', linewidth=2)
plt.title('(d) Fcn. Campana Generalizada')
plt.xlabel('Universo de Discurso')
plt.ylim(0, 1.1)
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()