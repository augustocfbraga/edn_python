# Solicitando o ano ao usuário
ano = int(input("Digite o ano que deseja verificar: "))

# Lógica de verificação
# 1. Divisível por 4
# 2. SE for centenário (divisível por 100), TEM QUE ser divisível por 400
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é BISSEXTO! 📅")
else:
    print(f"O ano {ano} NÃO é bissexto. ❌")
