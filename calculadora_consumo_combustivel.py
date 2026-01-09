# Dados da viagem
distancia = 300
combustivel_gasto = 25

# Cálculo do consumo médio (km dividido por litros)
consumo_medio = distancia / combustivel_gasto

# Exibição dos detalhes
print("--- Resumo da Viagem ---")
print(f"Distância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print("-" * 28)
print(f"Consumo médio: {consumo_medio:.2f} km/l")
