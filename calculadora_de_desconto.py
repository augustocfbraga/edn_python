# Informações do produto e desconto
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# Cálculo do valor do desconto
# (20% de 50.00)
valor_desconto = (preco_original * porcentagem_desconto) / 100

# Cálculo do preço final
# Preço original menos o valor do desconto
preco_final = preco_original - valor_desconto

# Exibição de todos os detalhes
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print("-" * 27)
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")
