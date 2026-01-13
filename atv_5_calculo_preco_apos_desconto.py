def calcular_preco_final():
    print("--- Calculadora de Descontos 2026 ---")
    
    try:
        # Interação com usuário (item d)
        preco_original = float(input("Digite o preço original do produto (R$): "))
        porcentagem_desconto = float(input("Digite a porcentagem de desconto (ex: 15 para 15%): "))

        # Cálculo de desconto (item a)
        valor_desconto = preco_original * (porcentagem_desconto / 100)

        # Preço final (item b)
        preco_final = preco_original - valor_desconto

        # Exibição e Formatação com 2 casas decimais (item c)
        print(f"\n--- Resumo da Compra ---")
        print(f"Preço Original: R$ {preco_original:.2f}")
        print(f"Desconto aplicado: R$ {valor_desconto:.2f} ({porcentagem_desconto}%)")
        print(f"Preço Final: R$ {preco_final:.2f}")
        print("------------------------")

    except ValueError:
        print("Erro: Por favor, insira apenas valores numéricos.")

if __name__ == "__main__":
    calcular_preco_final()
