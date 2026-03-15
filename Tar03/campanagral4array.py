import numpy as np


def campanaGauss(x, parametro):
    """
    FdM Gaussiana
    parametro: [centro, sigma]
    """
    mean = parametro[0]
    sigma = parametro[1]

    if isinstance(x, (int, float)):
        # Lógica Escalar
        return np.exp(-((x - mean) ** 2) / (2 * sigma ** 2))
    else:
        # Lógica Vectorizada
        return np.exp(-((x - mean) ** 2) / (2 * sigma ** 2))


def campanaGral(x, parametro):
    """
    FdM Campana Generalizada (Generalized Bell)
    parametro: [a, b, c]
      a: ancho
      b: pendiente
      c: centro
    """
    a = parametro[0]
    b = parametro[1]
    c = parametro[2]

    if isinstance(x, (int, float)):
        # Lógica Escalar
        # Agregamos abs() para evitar errores con números negativos elevados a potencias
        return 1 / (1 + abs((x - c) / a) ** (2 * b))
    else:
        # Lógica Vectorizada
        return 1 / (1 + np.abs((x - c) / a) ** (2 * b))


def sigmoidal(x, parametro):
    """
    FdM Sigmoidal (Extra para completar 5 funciones si se requiere)
    parametro: [a, c]
      a: pendiente (si es alta es más empinada)
      c: centro (punto de inflexión donde y=0.5)
    """
    a = parametro[0]
    c = parametro[1]

    # La formula es 1 / (1 + e^(-a * (x - c)))
    if isinstance(x, (int, float)):
        return 1 / (1 + np.exp(-a * (x - c)))
    else:
        return 1 / (1 + np.exp(-a * (x - c)))