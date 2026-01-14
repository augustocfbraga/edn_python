def ler_arquivo_usuario():
    # Solicita o nome do arquivo ao usuário
    nome_arquivo = input("Digite o nome do arquivo que deseja ler: ").strip()

    try:
        # Tenta abrir o arquivo para leitura ('r')
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            print(f"\n--- Conteúdo de '{nome_arquivo}' ---\n")
            
            # Percorre cada linha do arquivo
            for linha in arquivo:
                # O .strip() remove a quebra de linha extra ao imprimir
                print(linha.strip())
            
            print("\n" + "-" * (20 + len(nome_arquivo)))

    except FileNotFoundError:
        # Erro específico para quando o arquivo não existe no diretório
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    
    except Exception as e:
        # Captura outros erros genéricos (ex: falta de permissão)
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    ler_arquivo_usuario()
