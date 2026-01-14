import requests

def consultar_cep():
    cep = input("Digite o CEP (apenas números): ").strip().replace("-", "").replace(".", "")

    # Validação básica de formato
    if len(cep) != 8 or not cep.isdigit():
        print("Erro: Formato de CEP inválido. Digite 8 números.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Verifica erros de conexão/servidor
        
        dados = response.json()

        # A API retorna 'erro' em formato JSON se o CEP não existir
        if "erro" in dados:
            print("Falha: CEP não encontrado na base de dados.")
        else:
            print("\n--- Endereço Encontrado ---")
            print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
            print(f"Bairro:     {dados.get('bairro', 'N/A')}")
            print(f"Cidade:     {dados.get('localidade', 'N/A')}")
            print(f"Estado:     {dados.get('uf', 'N/A')}")

    except requests.exceptions.RequestException:
        print("Falha na requisição: Verifique sua conexão com a internet ou o serviço.")

if __name__ == "__main__":
    consultar_cep()
