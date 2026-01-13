def detalhar_servico(valor_conta, porcentagem_gorjeta):
    # Cálculo da gorjeta
    valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    # Cálculo do total
    total_geral = valor_conta + valor_gorjeta
    
    # Exibição discriminada (um embaixo do outro)
    print("\n--- EXTRATO DE PAGAMENTO ---")
    print(f"Consumo: R$ {valor_conta:.2f}")
    print(f"Gorjeta ({porcentagem_gorjeta}%): R$ {valor_gorjeta:.2f}")
    print("-" * 28)
    print(f"SOMA TOTAL: R$ {total_geral:.2f}")
    print("-" * 28)
    print("Obrigado pela preferência e volte sempre!")
    
    return valor_gorjeta, total_geral

# Execução
try:
    conta = float(input("Digite o valor total da conta: "))
    porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10): "))
    
    detalhar_servico(conta, porcentagem)
except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos.")

