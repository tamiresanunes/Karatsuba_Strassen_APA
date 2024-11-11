class Karatsuba:
    """
    Classe que implementa o algoritmo de multiplicação de Karatsuba.
    """

    @staticmethod
    def multiply(x, y):
        """
        Multiplica dois números inteiros x e y usando o algoritmo de Karatsuba.

        Parâmetros:
        x (int): O primeiro número a ser multiplicado.
        y (int): O segundo número a ser multiplicado.

        Retorna:
        int: O produto de x e y.
        """
        # Caso base: se x ou y forem menores que 10, retorna o produto diretamente
        if x < 10 or y < 10:
            return x * y

        # Calcula o número de dígitos e divide em duas partes
        n = max(len(str(x)), len(str(y)))
        m = n // 2

        # Divide x e y em partes
        high_x, low_x = divmod(x, 10**m)
        high_y, low_y = divmod(y, 10**m)

        # Realiza as multiplicações recursivas
        z0 = Karatsuba.multiply(low_x, low_y)
        z1 = Karatsuba.multiply(low_x + high_x, low_y + high_y)
        z2 = Karatsuba.multiply(high_x, high_y)

        # Combina os resultados
        return (z2 * 10**(2 * m)) + ((z1 - z2 - z0) * 10**m) + z0