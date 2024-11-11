from strassen import Strassen
import numpy as np

def main():
    """
    Função principal para testar a classe StrassenMultiplication.
    Executa a multiplicação de duas matrizes quadradas 2^n x 2^n e exibe o resultado.
    """
    # Define duas matrizes 4x4 para multiplicação
    A = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

    B = np.array([[16, 15, 14, 13],
                  [12, 11, 10, 9],
                  [8, 7, 6, 5],
                  [4, 3, 2, 1]])

    # Multiplica usando o algoritmo de Strassen
    resultado = Strassen.multiply(A, B)

    print("Resultado da multiplicação de A e B usando Strassen:")
    print(resultado)

if __name__ == "__main__":
    main()
