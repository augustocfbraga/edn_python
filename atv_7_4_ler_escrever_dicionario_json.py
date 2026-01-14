import json
import os

def processar_dados_json():
    # 1. Coleta os dados para o dicionário
    dados_pessoa = {
        "nome": input("Digite o nome: "),
        "idade": input("Digite a idade: "),
        "cidade": input("Digite a cidade: ")
    }
    
    nome_arquivo = input("Digite o nome do arquivo JSON (ex: dados.json): ").strip()
    if not nome_arquivo.endswith('.json'):
        nome_arquivo += '.json'

    # 2. Tenta salvar o dicionário no arquivo
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            # indent=4 deixa o arquivo legível para humanos
            json.dump(dados_pessoa, arquivo, indent=4, ensure_ascii=False)
        print(f"\n Sucesso: Dados salvos em '{nome_arquivo}'.")
    except Exception as e:
        print(f"Falha ao salvar o arquivo: {e}")
        return # Interrompe o programa se não conseguir salvar

    # 3. Tenta ler o arquivo e exibir os dados
    print("\n--- Lendo dados do arquivo ---")
    try:
        # Verifica se o arquivo existe antes de tentar abrir
        if not os.path.exists(nome_arquivo):
            raise FileNotFoundError(f"O arquivo '{nome_arquivo}' não foi encontrado.")

        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados_lidos = json.load(arquivo)
            
            print(f"Nome: {dados_lidos['nome']}")
            print(f"Idade: {dados_lidos['idade']}")
            print(f"Cidade: {dados_lidos['cidade']}")
            
    except FileNotFoundError as e:
        print(f"Erro de Leitura: {e}")
    except json.JSONDecodeError:
        print("Erro: O arquivo existe, mas não está em um formato JSON válido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado na leitura: {e}")

if __name__ == "__main__":
    processar_dados_json()
