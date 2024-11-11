import numpy as np

class Strassen:
    """
    Classe para multiplicação de matrizes usando o algoritmo de Strassen.
    """

    @staticmethod
    def multiply(A, B):
        """
        Multiplica duas matrizes quadradas de tamanho 2^n x 2^n usando o algoritmo de Strassen.

        Parâmetros:
        A (np.array): A primeira matriz (2^n x 2^n).
        B (np.array): A segunda matriz (2^n x 2^n).

        Retorna:
        np.array: A matriz produto resultante de A * B.
        """
        # Caso base: se as matrizes são 1x1
        if A.shape[0] == 1:
            return A * B

        # Divide as matrizes em quadrantes
        a11, a12, a21, a22 = Strassen.split(A)
        b11, b12, b21, b22 = Strassen.split(B)

        # Calcula os produtos de Strassen
        m1 = Strassen.multiply(a11 + a22, b11 + b22)
        m2 = Strassen.multiply(a21 + a22, b11)
        m3 = Strassen.multiply(a11, b12 - b22)
        m4 = Strassen.multiply(a22, b21 - b11)
        m5 = Strassen.multiply(a11 + a12, b22)
        m6 = Strassen.multiply(a21 - a11, b11 + b12)
        m7 = Strassen.multiply(a12 - a22, b21 + b22)

        # Combina os produtos em quadrantes da matriz resultante
        c11 = m1 + m4 - m5 + m7
        c12 = m3 + m5
        c21 = m2 + m4
        c22 = m1 - m2 + m3 + m6

        # Combina os quadrantes em uma única matriz
        return Strassen.combine(c11, c12, c21, c22)

    @staticmethod
    def split(matrix):
        """
        Divide uma matriz em quatro submatrizes quadrantes.

        Parâmetros:
        matrix (np.array): A matriz a ser dividida.

        Retorna:
        tuple: Quatro submatrizes resultantes da divisão.
        """
        row, col = matrix.shape
        mid = row // 2
        return matrix[:mid, :mid], matrix[:mid, mid:], matrix[mid:, :mid], matrix[mid:, mid:]

    @staticmethod
    def combine(c11, c12, c21, c22):
        """
        Combina quatro submatrizes em uma única matriz.

        Parâmetros:
        c11, c12, c21, c22 (np.array): As quatro submatrizes.

        Retorna:
        np.array: A matriz combinada resultante.
        """
        top = np.hstack((c11, c12))
        bottom = np.hstack((c21, c22))
        return np.vstack((top, bottom))
