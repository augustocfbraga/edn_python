import string
import secrets

def gerar_senha(tamanho):
    # Define os caracteres: letras (maiúsculas e minúsculas), números e pontuação
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera a senha de forma segura para criptografia
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

# Interação com o usuário
try:
    comprimento = int(input("Digite o tamanho da senha desejada: "))
    if comprimento < 4:
        print("Para sua segurança, tente uma senha com pelo menos 8 caracteres.")
    else:
        print(f"Sua senha segura é: {gerar_senha(comprimento)}")
except ValueError:
    print("Por favor, digite apenas números inteiros.")
