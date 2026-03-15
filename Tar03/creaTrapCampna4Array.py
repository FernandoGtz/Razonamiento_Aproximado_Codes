import numpy as np
import matplotlib.pyplot as plt
# Importamos tus librerías personalizadas
import trap_fdm4array as mis_trapecios
import campanagral4array as mis_campanas


def main():
    print("   SISTEMA DE RAZONAMIENTO APROXIMADO   ")
    print("Seleccione una opción:")
    print("1. Graficar una Función de Membresía (Diseño)")
    print("2. Evaluar un valor 'x' (Modo Usuario/Prueba)")

    opcion = input(">> Ingrese su opción (1 o 2): ")

    # OPCIÓN 1: GRAFICAR FUNCIONES
    if opcion == '1':
        print("Seleccione el tipo de función:")
        print("a. Triangular")
        print("b. Trapezoidal")
        print("c. Gaussiana")
        print("d. Campana Generalizada")
        print("e. Sigmoidal")

        tipo = input(">> Tipo de función (a/b/c/d/e): ").lower()

        # Definir el Universo de Discurso (Eje X)
        print("\nDefina el rango del eje X (Universo de Discurso):")
        try:
            inicio = float(input("Inicio (ej. 0): "))
            fin = float(input("Fin (ej. 100): "))
            paso = 0.1
            x_vector = np.arange(inicio, fin + paso, paso)
        except ValueError:
            print("Error: Por favor ingrese números válidos.")
            return

        y_vector = None
        titulo = ""

        # Pedir parámetros y calcular según la función
        if tipo == 'a':  # Triangular
            print("\nParámetros Triangular (a < b < c):")
            pa = float(input("a (inicio): "))
            pb = float(input("b (pico): "))
            pc = float(input("c (fin): "))
            y_vector = mis_trapecios.triangular(x_vector, [pa, pb, pc])
            titulo = f"Triangular (a={pa}, b={pb}, c={pc})"

        elif tipo == 'b':  # Trapezoidal
            print("\nParámetros Trapezoidal (a < b < c < d):")
            pa = float(input("a (pie izq): "))
            pb = float(input("b (hombro izq): "))
            pc = float(input("c (hombro der): "))
            pd = float(input("d (pie der): "))
            y_vector = mis_trapecios.trapezoide(x_vector, [pa, pb, pc, pd])
            titulo = f"Trapezoidal (a={pa}, b={pb}, c={pc}, d={pd})"

        elif tipo == 'c':  # Gaussiana
            print("\nParámetros Gaussiana:")
            mean = float(input("Centro (media): "))
            sigma = float(input("Desviación (ancho): "))
            y_vector = mis_campanas.campanaGauss(x_vector, [mean, sigma])
            titulo = f"Gaussiana (c={mean}, sigma={sigma})"

        elif tipo == 'd':  # Campana Gral
            print("\nParámetros Campana Generalizada:")
            a = float(input("a (ancho): "))
            b = float(input("b (pendiente): "))
            c = float(input("c (centro): "))
            y_vector = mis_campanas.campanaGral(x_vector, [a, b, c])
            titulo = f"Campana Gral (a={a}, b={b}, c={c})"

        elif tipo == 'e':  # Sigmoidal
            print("\nParámetros Sigmoidal:")
            a = float(input("a (pendiente, ej. 0.5): "))
            c = float(input("c (centro, ej. 50): "))
            y_vector = mis_campanas.sigmoidal(x_vector, [a, c])
            titulo = f"Sigmoidal (a={a}, c={c})"

        else:
            print("Opción no válida.")
            return

        # Graficar
        plt.figure(figsize=(8, 6))
        plt.plot(x_vector, y_vector, linewidth=2, color='blue')
        plt.title(titulo)
        plt.xlabel('Universo X')
        plt.ylabel(r'Membresía $\mu(x)$')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.ylim(-0.05, 1.05)
        plt.show()

    # OPCIÓN 2: EVALUAR MU X
    elif opcion == '2':
        try:
            val_x = float(input(">> Ingrese el valor de x a evaluar: "))
        except ValueError:
            print("Error: Valor numérico requerido.")
            return

        # Parámetros Estándar
        p_tri = [10, 40, 70]  # Triangular
        p_trap = [20, 40, 60, 90]  # Trapezoidal
        p_gauss = [50, 15]  # Gaussiana
        p_bell = [20, 4, 50]  # Campana Gral
        p_sig = [0.2, 50]  # Sigmoidal

        # CÁLCULO ESCALAR
        mu_tri = mis_trapecios.triangular(val_x, p_tri)
        mu_trap = mis_trapecios.trapezoide(val_x, p_trap)
        mu_gauss = mis_campanas.campanaGauss(val_x, p_gauss)
        mu_bell = mis_campanas.campanaGral(val_x, p_bell)
        mu_sig = mis_campanas.sigmoidal(val_x, p_sig)

        # Reporte textual
        print(f"\nResultados de Membresía para x = {val_x}:")
        print("-" * 40)
        print(f"1. Triangular (Estándar): \t{mu_tri:.4f}")
        print(f"2. Trapezoidal (Estándar): \t{mu_trap:.4f}")
        print(f"3. Gaussiana (Estándar):  \t{mu_gauss:.4f}")
        print(f"4. Campana Gral (Estándar): \t{mu_bell:.4f}")
        print(f"5. Sigmoidal (Estándar):    \t{mu_sig:.4f}")
        print("-" * 40)
        print("Mostrando gráficas de referencia...")

        # Generar Gráficas de Referencia
        # Cambiamos a subplots 2x3 para que quepan las 5 gráficas
        x_univ = np.arange(0, 101, 0.5)

        y_tri = mis_trapecios.triangular(x_univ, p_tri)
        y_trap = mis_trapecios.trapezoide(x_univ, p_trap)
        y_gauss = mis_campanas.campanaGauss(x_univ, p_gauss)
        y_bell = mis_campanas.campanaGral(x_univ, p_bell)
        y_sig = mis_campanas.sigmoidal(x_univ, p_sig)

        plt.figure(figsize=(12, 8))

        # Subplot 1: Triangular
        plt.subplot(2, 3, 1)
        plt.plot(x_univ, y_tri, 'b')
        plt.plot(val_x, mu_tri, 'ro')
        plt.title(rf'Triangular (x={val_x}, $\mu$={mu_tri:.2f})')
        plt.grid(True)

        # Subplot 2: Trapezoidal
        plt.subplot(2, 3, 2)
        plt.plot(x_univ, y_trap, 'g')
        plt.plot(val_x, mu_trap, 'ro')
        plt.title(rf'Trapezoidal (x={val_x}, $\mu$={mu_trap:.2f})')
        plt.grid(True)

        # Subplot 3: Gaussiana
        plt.subplot(2, 3, 3)
        plt.plot(x_univ, y_gauss, 'm')
        plt.plot(val_x, mu_gauss, 'ro')
        plt.title(rf'Gaussiana (x={val_x}, $\mu$={mu_gauss:.2f})')
        plt.grid(True)

        # Subplot 4: Campana Gral
        plt.subplot(2, 3, 4)
        plt.plot(x_univ, y_bell, 'c')
        plt.plot(val_x, mu_bell, 'ro')
        plt.title(rf'Campana Gral (x={val_x}, $\mu$={mu_bell:.2f})')
        plt.grid(True)

        # Subplot 5: Sigmoidal
        plt.subplot(2, 3, 5)
        plt.plot(x_univ, y_sig, 'k')
        plt.plot(val_x, mu_sig, 'ro')
        plt.title(rf'Sigmoidal (x={val_x}, $\mu$={mu_sig:.2f})')
        plt.grid(True)

        # Ajuste de diseño
        plt.tight_layout()
        plt.show()

    else:
        print("Opción desconocida.")


if __name__ == "__main__":
    main()