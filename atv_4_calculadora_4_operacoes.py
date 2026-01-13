def calculadora():
    print("--- Calculadora Python 2026 ---")
    print("Operações: + (Soma), - (Subtração), * (Multiplicação), / (Divisão)")
    print("Digite 'sair' para encerrar.")

    while True:
        entrada = input("\nEscolha a operação ou 'sair': ").lower()
        
        if entrada == 'sair':
            print("Até logo!")
            break
        
        if entrada in ('+', '-', '*', '/'):
            try:
                num1 = float(input("Primeiro número: "))
                num2 = float(input("Segundo número: "))

                if entrada == '+':
                    print(f"Resultado: {num1 + num2}")
                elif entrada == '-':
                    print(f"Resultado: {num1 - num2}")
                elif entrada == '*':
                    print(f"Resultado: {num1 * num2}")
                elif entrada == '/':
                    if num2 == 0:
                        print("Erro: Divisão por zero não permitida!")
                    else:
                        print(f"Resultado: {num1 / num2}")
            except ValueError:
                print("Erro: Por favor, digite apenas números.")
        else:
            print("Operação inválida. Tente novamente.")

if __name__ == "__main__":
    calculadora()
