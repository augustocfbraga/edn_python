import requests 
import os
import sys

os.system('clear')

print("--- MENU DE OPÇÕES ---")
print("Escolha uma opção para ver a cotação em Reais (BRL), ou <ENTER> p sair:")
print("1. USD")
print("2. EUR")
print("3. BTC")

while True:
    escolha = input("Escolha a moeda: ")
    if escolha == "":
        print("Saindo do programa.")
        break
        
    if escolha == "1":
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        response = requests.get(url)
        dados = response.json()
        bid = dados["USDBRL"]["bid"]
        high = dados["USDBRL"]["high"]
        low = dados["USDBRL"]["low"]
        data_hora = dados["USDBRL"]['create_date']
        print(f"O valor atual do Dólar é: R$ {bid:.4}")
        print(f"O valor máximo do Dólar na alta é: R$ {high:.4}")
        print(f"O valor mínimo do Dólar na baixa é: R$ {low:.4}")
        print(f"Última Atualização: {data_hora}")
        #break

    if escolha == "2":
        url = "https://economia.awesomeapi.com.br/json/last/EUR-BRL"
        response = requests.get(url)
        dados = response.json()
        bid = dados["EURBRL"]["bid"]
        high = dados["EURBRL"]["high"]
        low = dados["EURBRL"]["low"]
        data_hora = dados["EURBRL"]['create_date']
        print(f"O valor atual do Euro é: R$ {bid:.4}")
        print(f"O valor máximo do Euro na alta é: R$ {high:.4}")
        print(f"O valor mínimo do Euro na baixa é: R$ {low:.4}")
        print(f"Última Atualização: {data_hora}")
        #break
       
    if escolha == "3":
        url = "https://economia.awesomeapi.com.br/json/last/BTC-BRL"
        response = requests.get(url)
        dados = response.json()
        bid = dados["BTCBRL"]["bid"]
        high = dados["BTCBRL"]["high"]
        low = dados["BTCBRL"]["low"]
        data_hora = dados["BTCBRL"]['create_date']
        print(f"O valor atual da Bitcoin é: R$ {bid:4}")
        print(f"O valor máximo da Bitcoin na alta é: R$ {high:4}")
        print(f"O valor mínimo da Bitcoin na baixa é: R$ {low:4}")
        print(f"Última Atualização: {data_hora}")
        #break

else:
    print("Opção inválida. Digite apenas de 1 - 3!")

  
        
