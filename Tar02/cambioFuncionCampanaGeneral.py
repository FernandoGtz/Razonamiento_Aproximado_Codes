# cambioFcnCampGral.py
# Programa para visualizar el efecto de los parámetros a, b y c
# en la función de membresía de Campana Generalizada.
# Basado en la Figura 2.8 de libros de texto de Lógica Difusa.

import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

# 1. Definición de la Función Campana Generalizada
def gbell_mf(x, a, b, c):
    """
    a: Ancho de la campana
    b: Pendiente (forma de la curva)
    c: Centro
    """
    return 1 / (1 + np.abs((x - c) / a) ** (2 * b))

# 2. Universo de Discurso
# Ampliamos el rango de -20 a 20 para ver bien las gráficas centradas en 0 y -5
x = np.arange(-20, 20.1, 0.1)

# --- 3. Configuración de la ventana ---
plt.figure(figsize=(10, 8))

# CASO (a): Variando 'a' (ancho)
# b = 2; c = 0; a = 2, 4, 6
plt.subplot(2, 2, 1)
params_a = [2, 4, 6]
b_fixed = 2
c_fixed = 0

for a in params_a:
    y = gbell_mf(x, a, b_fixed, c_fixed)
    plt.plot(x, y, label=f'a={a}')

plt.title('(a) Variando "a" (ancho)')
plt.ylabel('Membresía')
plt.ylim(0, 1.1)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)


# CASO (b): Variando 'b' (pendiente)
# a = 5; c = 0; b = 1, 2, 4
plt.subplot(2, 2, 2)
params_b = [1, 2, 4]
a_fixed = 5
c_fixed = 0

for b in params_b:
    y = gbell_mf(x, a_fixed, b, c_fixed)
    plt.plot(x, y, label=f'b={b}')

plt.title('(b) Variando "b" (pendiente)')
plt.ylim(0, 1.1)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)


# CASO (c): Variando 'c' (centro)
# a = 5; b = 2; c = -5, 0, 5
plt.subplot(2, 2, 3)
params_c = [-5, 0, 5]
a_fixed = 5
b_fixed = 2

for c in params_c:
    y = gbell_mf(x, a_fixed, b_fixed, c)
    plt.plot(x, y, label=f'c={c}')

plt.title('(c) Variando "c" (centro)')
plt.ylabel('Membresía')
plt.xlabel('x')
plt.ylim(0, 1.1)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)


# CASO (d): Variando 'a' y 'b' simultáneamente
# c = 0; Pares: (a=4, b=4), (a=6, b=6), (a=8, b=8)
plt.subplot(2, 2, 4)
pairs = [(4, 4), (6, 6), (8, 8)] # Lista de tuplas (a, b)
c_fixed = 0

for a, b in pairs:
    y = gbell_mf(x, a, b, c_fixed)
    plt.plot(x, y, label=f'a={a}, b={b}')

plt.title('(d) Variando "a" y "b"')
plt.xlabel('x')
plt.ylim(0, 1.1)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

#Mostrar gráficas
plt.tight_layout()
plt.show()