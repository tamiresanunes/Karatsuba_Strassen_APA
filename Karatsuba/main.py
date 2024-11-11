from karatsuba import Karatsuba

def main():
    """
    Função principal para testar a classe karatsuba.
    Executa alguns testes para verificar se a implementação do algoritmo de Karatsuba está correta.
    """
    # Casos de teste
    testes = [
        (1234, 5678, 7006652),
        (12, 34, 408),
        (5, 8, 40),
        (987654321, 123456789, 121932631112635269),
        (123456789012345678, 987654321987654321, 121932631137021795226097227107703609)
    ]

    # Executa cada teste e verifica se o resultado é o esperado
    for x, y, esperado in testes:
        resultado = Karatsuba.multiply(x, y)
        if resultado == esperado:
            print(f"Teste para {x} * {y} passou! Resultado: {resultado}")
        else:
            print(f"Teste para {x} * {y} falhou. Resultado: {resultado}, Esperado: {esperado}")

if __name__ == "__main__":
    main()
