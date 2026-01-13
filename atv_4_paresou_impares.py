def analisar_numeros():
    pares = 0
    impares = 0
    
    print("--- Analisador de Números 2026 ---")
    print("Digite os números que desejar (ou '0' para encerrar):")

    while True:
        try:
            num = int(input("Digite um número: "))
            
            if num == 0:
                break
            
            if num % 2 == 0:
                print(f"O número {num} é PAR.")
                pares += 1
            else:
                print(f"O número {num} é ÍMPAR.")
                impares += 1
                
        except ValueError:
            print("Erro: Por favor, digite apenas números inteiros.")

    print("\n--- Resumo Final ---")
    print(f"Quantidade de Pares: {pares}")
    print(f"Quantidade de Ímpares: {impares}")
    print(f"Total de números analisados: {pares + impares}")

if __name__ == "__main__":
    analisar_numeros()
