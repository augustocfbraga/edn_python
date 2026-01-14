import requests

def buscar_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    
    try:
        # Faz a requisição à API
        resposta = requests.get(url, timeout=10)
        
        # Verifica se houve erro no status HTTP (ex: 404 ou 500)
        resposta.raise_for_status()
        
        # Converte a resposta para JSON
        dados = resposta.json()
        usuario = dados['results'][0]
        
        # Extrai as informações solicitadas
        nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        # Exibe os dados
        print("--- Usuário Fictício Encontrado ---")
        print(f"Nome: {nome_completo}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException as e:
        # Captura falhas de conexão, timeout ou erros de HTTP
        print(f"Falha na conexão: Não foi possível acessar a API.")
        print(f"Detalhes do erro: {e}")

if __name__ == "__main__":
    buscar_usuario_aleatorio()
