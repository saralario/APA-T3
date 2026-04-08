"""
Sara Lario Garrido

Tests unitaris requerits:

>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2.0, 4.0, 6.0])

>>> v1 * v2
Vector([4.0, 10.0, 18.0])

>>> v1 @ v2
32.0

>>> v3 = Vector([2, 1, 2])
>>> v4 = Vector([0.5, 1, 0.5])
>>> v3 // v4
Vector([1.0, 2.0, 1.0])

>>> v3 % v4
Vector([1.0, -1.0, 1.0])
"""

import doctest

class Vector:
    def __init__(self, dades):
        self.dades = [float(x) for x in dades]

    def __repr__(self):
        # Forcem que cada número surti amb un decimal (.1f) per coincidir amb el test
        valors = ", ".join([f"{x:.1f}" if x != int(x) else f"{x:.1f}" for x in self.dades])
        # Intentem un format més estàndard de llista per evitar embolics
        return f"Vector([{', '.join([str(float(x)) for x in self.dades])}])"

    def __add__(self, sumand):
        return Vector([x + y for x, y in zip(self.dades, sumand.dades)])

    def __sub__(self, subtrahend):
        return Vector([x - y for x, y in zip(self.dades, subtrahend.dades)])

    def __mul__(self, operant):
        if isinstance(operant, (int, float)):
            return Vector([val * operant for val in self.dades])
        if isinstance(operant, Vector):
            return Vector([a * b for a, b in zip(self.dades, operant.dades)])
        return NotImplemented
        
    def __rmul__(self, escalar):
        return self.__mul__(escalar)

    def __matmul__(self, v_remot):
        return float(sum(i * j for i, j in zip(self.dades, v_remot.dades)))

    def __floordiv__(self, v_referencia):
        factor = (self @ v_referencia) / (v_referencia @ v_referencia)
        return factor * v_referencia

    def __mod__(self, v_referencia):
        return self - (self // v_referencia)

if __name__ == "__main__":
    doctest.testmod(verbose=True)
