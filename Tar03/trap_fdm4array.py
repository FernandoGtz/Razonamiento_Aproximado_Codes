import numpy as np


def triangular(x, parametro):
    """
    Calcula la FdM Triangular.
    parametro: [a, b, c]
      a: inicio
      b: pico
      c: fin
    """
    # Desempaquetamos parámetros para claridad
    a = parametro[0]
    b = parametro[1]
    c = parametro[2]

    if isinstance(x, (int, float)):
        # Lógica para ESCALAR (un solo número)
        if x <= a:
            return 0.0
        elif a < x <= b:
            return (x - a) / (b - a)
        elif b < x < c:
            return (c - x) / (c - b)
        else:
            return 0.0

    else:
        # Lógica para ARREGLO
        return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))


def trapezoide(x, parametro):
    """
    Calcula la FdM Trapezoidal.
    parametro: [a, b, c, d]
      a: inicio subida
      b: fin subida (inicio plano)
      c: inicio bajada (fin plano)
      d: fin bajada
    """
    a = parametro[0]
    b = parametro[1]
    c = parametro[2]
    d = parametro[3]

    if isinstance(x, (int, float)):
        # Lógica Escalar
        if x <= a:
            return 0.0
        elif a < x < b:
            return (x - a) / (b - a)
        elif b <= x <= c:
            return 1.0
        elif c < x < d:
            return (d - x) / (d - c)
        else:
            return 0.0
    else:
        # Lógica Vectorizada
        term1 = (x - a) / (b - a)
        term2 = (d - x) / (d - c)
        return np.maximum(0, np.minimum(np.minimum(term1, 1), term2))