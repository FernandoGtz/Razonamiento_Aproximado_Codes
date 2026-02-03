# variantesSigmoidales.py
# Programa para visualizar variantes de funciones de membresía Sigmoidales
# Basado en la Figura 2.10 del libro "Neuro-Fuzzy and Soft Computing"

import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

# 1. Definición de las Funciones Matemáticas

def sigmf(x, a, c):
    """
    Función Sigmoidal básica.
    a: controla la pendiente (positivo=crece, negativo=decrece)
    c: punto de cruce (donde y = 0.5)
    """
    return 1 / (1 + np.exp(-a * (x - c)))

def dsigmf(x, a1, c1, a2, c2):
    """
    Diferencia de dos funciones sigmoidales.
    f(x) = sigmf1(x) - sigmf2(x)
    """
    return sigmf(x, a1, c1) - sigmf(x, a2, c2)

def psigmf(x, a1, c1, a2, c2):
    """
    Producto de dos funciones sigmoidales.
    f(x) = sigmf1(x) * sigmf2(x)
    Usado para crear campanas asimétricas suaves.
    """
    return sigmf(x, a1, c1) * sigmf(x, a2, c2)

# 2. Universo de Discurso
# Rango amplio (-20 a 20) para ver el comportamiento completo
x = np.arange(-20, 20.1, 0.1)

# 3. Gráficas
plt.figure(figsize=(10, 8))

# (a) Sigmoides Simples (Abierta izq y der)
plt.subplot(2, 2, 1)
# Sigmoide 1: a=1 (sube), c=-5
y1 = sigmf(x, a=1, c=-5)
# Sigmoide 2: a=-2 (baja rápido), c=5
y2 = sigmf(x, a=-2, c=5)

plt.plot(x, y1, label='a=1, c=-5')
plt.plot(x, y2, '--', label='a=-2, c=5')
plt.title('(a) Funciones Sigmoidales Simples')
plt.ylabel('Grados de Membresía')
plt.legend()
plt.ylim(0, 1.1)
plt.grid(True, linestyle='--', alpha=0.5)

# (b) Diferencia de dos Sigmoides (dsigmf)
plt.subplot(2, 2, 2)
# Para crear una "loma" restando:
# La primera sube en -5, la segunda sube en 5.
# Al restar la segunda de la primera, la parte derecha se cancela.
y_diff = dsigmf(x, a1=1, c1=-5, a2=1, c2=5)

plt.plot(x, y_diff, color='purple', label='a1=1, c1=-5, a2=1, c2=5')
plt.title('(b) Diferencia de dos Sigmoides (dsigmf)')
plt.legend()
plt.ylim(0, 1.1)
plt.grid(True, linestyle='--', alpha=0.5)

# (c) Producto de dos Sigmoides (psigmf) - Simétrico
plt.subplot(2, 2, 3)
# Multiplicamos una que sube (a=2) por una que baja (a=-2)
y_prod1 = psigmf(x, a1=2, c1=-5, a2=-2, c2=5)

plt.plot(x, y_prod1, color='green', label='a1=2, c1=-5, a2=-2, c2=5')
plt.title('(c) Producto de dos Sigmoides (psigmf)')
plt.xlabel('x')
plt.ylabel('Grados de Membresía')
plt.legend(loc='upper right')
plt.ylim(0, 1.1)
plt.grid(True, linestyle='--', alpha=0.5)

# (d) Producto de dos Sigmoides (psigmf) - Asimétrico
plt.subplot(2, 2, 4)
# Sube suave (a=1) y cae muy abruptamente (a=-5)
y_prod2 = psigmf(x, a1=1, c1=-5, a2=-5, c2=5)

plt.plot(x, y_prod2, color='red', label='a1=1, c1=-5, a2=-5, c2=5')
plt.title('(d) Producto Asimétrico')
plt.xlabel('x')
plt.legend()
plt.ylim(0, 1.1)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()