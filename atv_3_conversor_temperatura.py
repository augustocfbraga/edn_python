def converter_temperatura():
    print("--- Conversor de Temperaturas ---")
    
    try:
        temp = float(input("Digite a temperatura: "))
        origem = input("Unidade de origem (C, F, K): ").upper().strip()
        destino = input("Unidade de destino (C, F, K): ").upper().strip()

        # Primeiro: Converte tudo para Celsius (Base)
        if origem == "C":
            celsius = temp
        elif origem == "F":
            celsius = (temp - 32) * 5/9
        elif origem == "K":
            celsius = temp - 273.15
        else:
            return "Unidade de origem inválida!"

        # Segundo: Converte de Celsius para o Destino
        if destino == "C":
            resultado = celsius
        elif destino == "F":
            resultado = (celsius * 9/5) + 32
        elif destino == "K":
            resultado = celsius + 273.15
        else:
            return "Unidade de destino inválida!"

        print(f"\nResultado: {temp}{origem} equivale a {resultado:.2f}{destino}")

    except ValueError:
        print("Erro: Por favor, insira apenas números para a temperatura.")

if __name__ == "__main__":
    converter_temperatura()
