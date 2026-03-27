import numpy as np
import matplotlib.pyplot as plt

# 1. Datos experimentales
force = np.array([1.1, 1.9, 3.2, 4.4, 5.9, 7.4, 9.2])
leng  = np.array([1.5, 2.1, 2.5, 3.3, 4.1, 4.6, 5.0])

# Vector continuo para graficar
x_graf = np.arange(0, 10.1, 0.1)

# 2. Ajuste polinomial (equivalente a polyfit)
coef1 = np.polyfit(force, leng, 1)
coef2 = np.polyfit(force, leng, 2)
coef3 = np.polyfit(force, leng, 3)
coef4 = np.polyfit(force, leng, 4)

# 3. Evaluación de polinomios
# A) Para graficar
y1_graf = np.polyval(coef1, x_graf)
y2_graf = np.polyval(coef2, x_graf)
y3_graf = np.polyval(coef3, x_graf)
y4_graf = np.polyval(coef4, x_graf)

# B) Para calcular error (en puntos originales)
y1_est = np.polyval(coef1, force)
y2_est = np.polyval(coef2, force)
y3_est = np.polyval(coef3, force)
y4_est = np.polyval(coef4, force)

# 4. Error (e = real - estimado)
e1 = leng - y1_est
e2 = leng - y2_est
e3 = leng - y3_est
e4 = leng - y4_est

# 5. SSE (Sum of Squared Errors)
sse1 = np.sum(e1**2)
sse2 = np.sum(e2**2)
sse3 = np.sum(e3**2)
sse4 = np.sum(e4**2)

# 6. Mostrar resultados
print('--- RESULTADOS DE ERROR CUADRÁTICO (SSE) ---')
print(f'Orden 1 (Lineal): {sse1:.6f}')
print(f'Orden 2 (Cuadrático): {sse2:.6f}')
print(f'Orden 3 (Cúbico): {sse3:.6f}')
print(f'Orden 4 (Cuártico): {sse4:.6f}')

print('\n--- VECTORES DE ERROR ---')
print('   Error Ord 1    Error Ord 2    Error Ord 3    Error Ord 4')
print(np.column_stack((e1, e2, e3, e4)))

# 7. Gráficas
plt.figure(figsize=(10, 8))

# Orden 1
plt.subplot(2, 2, 1)
plt.plot(x_graf, y1_graf)
plt.plot(force, leng, 'o')
plt.title(f'(a) 1er Orden | SSE: {sse1:.4f}')
plt.xlabel('Fuerza')
plt.ylabel('Longitud')
plt.grid()

# Orden 2
plt.subplot(2, 2, 2)
plt.plot(x_graf, y2_graf)
plt.plot(force, leng, 'o')
plt.title(f'(b) 2do Orden | SSE: {sse2:.4f}')
plt.xlabel('Fuerza')
plt.ylabel('Longitud')
plt.grid()

# Orden 3
plt.subplot(2, 2, 3)
plt.plot(x_graf, y3_graf)
plt.plot(force, leng, 'o')
plt.title(f'(c) 3er Orden | SSE: {sse3:.4f}')
plt.xlabel('Fuerza')
plt.ylabel('Longitud')
plt.grid()

# Orden 4
plt.subplot(2, 2, 4)
plt.plot(x_graf, y4_graf)
plt.plot(force, leng, 'o')
plt.title(f'(d) 4to Orden | SSE: {sse4:.4f}')
plt.xlabel('Fuerza')
plt.ylabel('Longitud')
plt.grid()

plt.tight_layout()
plt.show()