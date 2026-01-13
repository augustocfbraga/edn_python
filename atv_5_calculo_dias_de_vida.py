from datetime import date

def calcular_dias_vividos():
    print("--- Calculadora de Dias Vividos 2026 ---")
    
    try:
        # Solicitando os dados do usuário
        dia = int(input("Dia do nascimento (DD): "))
        mes = int(input("Mês do nascimento (MM): "))
        ano = int(input("Ano do nascimento (AAAA): "))

        # Definindo a data de nascimento e a data de hoje (13/01/2026)
        data_nascimento = date(ano, mes, dia)
        hoje = date.today() # Captura automaticamente 13/01/2026

        # Calculando a diferença
        diferenca = hoje - data_nascimento

        if diferenca.days < 0:
            print("Peraí! Essa data ainda não chegou. Você é do futuro? 🚀")
        else:
            print(f"\nVocê nasceu em: {data_nascimento.strftime('%d/%m/%Y')}")
            print(f"Hoje é: {hoje.strftime('%d/%m/%Y')}")
            print(f"Você está vivo há exatamente: {diferenca.days:,} dias!".replace(',', '.'))

    except ValueError:
        print("Erro: Data inválida. Certifique-se de digitar números reais para dia, mês e ano.")

if __name__ == "__main__":
    calcular_dias_vividos() #apreesentacao
