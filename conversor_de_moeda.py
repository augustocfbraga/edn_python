# Dados iniciais
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

# Cálculos de conversão
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

# Exibição dos resultados com 2 casas decimais
print(f"Valor em Reais: R$ {valor_reais:.2f}")
print(f"Conversão para Dólar: $ {valor_dolar:.2f}")
print(f"Conversão para Euro: € {valor_euro:.2f}")
