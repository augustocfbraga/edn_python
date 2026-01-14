import pandas as pd
import os

def analisar_tempos_execucao(nome_arquivo):
    """
    Lê um arquivo CSV, calcula a média e o desvio padrão da coluna 'tempo_execucao'.

    Args:
        nome_arquivo (str): O nome do arquivo CSV a ser lido.
    """
    # Verifica se o arquivo existe antes de tentar ler (alternativa ao try/except básico)
    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return

    try:
        # Tenta ler o arquivo CSV
        df = pd.read_csv(nome_arquivo)

        # Verifica se a coluna 'tempo_execucao' existe no DataFrame
        if 'tempo_execucao' in df.columns:
            # Calcula a média e o desvio padrão da coluna específica
            media = df['tempo_execucao'].mean()
            desvio_padrao = df['tempo_execucao'].std()

            print(f"Análise para o arquivo: '{nome_arquivo}'")
            print(f"Média do tempo de execução: {media:.2f}")
            print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f}")
        else:
            print(f"Erro: A coluna 'tempo_execucao' não foi encontrada no arquivo '{nome_arquivo}'.")

    except pd.errors.EmptyDataError:
        print(f"Erro: O arquivo '{nome_arquivo}' está vazio.")
    except pd.errors.ParserError:
        print(f"Erro: Problema ao analisar o arquivo '{nome_arquivo}'. Verifique o formato CSV (delimitador, aspas, etc.).")
    except Exception as e:
        print(f"Ocorreu um erro inesperado durante a leitura/análise do arquivo: {e}")

# Exemplo de uso:
# Crie um arquivo CSV de teste chamado "dados_execucao.csv" com o seguinte conteúdo:
# tempo_execucao,tarefa
# 10.5,A
# 12.1,B
# 11.8,C
# 10.2,D
# 13.5,E

# Nome do arquivo a ser analisado
arquivo_csv = "dados_execucao.csv"

# Chama a função para realizar a análise
analisar_tempos_execucao(arquivo_csv)
