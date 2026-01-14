import os

def criar_arquivo_tabular():
    # Coleta de dados
    pessoas = [
        {"Nome": "Ana Silva", "Idade": 28, "Cidade": "São Paulo"},
        {"Nome": "Bruno Costa", "Idade": 34, "Cidade": "Rio de Janeiro"},
        {"Nome": "Carla Souza", "Idade": 22, "Cidade": "Curitiba"}
    ]

    # Solicita o nome do arquivo ao usuário
    nome_arquivo = input("Digite o nome do arquivo para salvar (ex: dados.txt): ").strip()

    try:
        # Tenta abrir o arquivo para escrita
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            # Cabeçalho da tabela
            header = f"{'Nome':<20} | {'Idade':<5} | {'Cidade':<20}\n"
            separator = "-" * 50 + "\n"
            
            arquivo.write(header)
            arquivo.write(separator)

            # Escreve os dados de cada pessoa
            for p in pessoas:
                linha = f"{p['Nome']:<20} | {p['Idade']:<5} | {p['Cidade']:<20}\n"
                arquivo.write(linha)
        
        print(f"Sucesso! Arquivo '{nome_arquivo}' criado com os dados tabulados.")

    except Exception as e:
        # Caso ocorra qualquer erro (permissão, caminho inválido, etc)
        print(f"Falha ao salvar o arquivo: {e}")

if __name__ == "__main__":
    criar_arquivo_tabular()
