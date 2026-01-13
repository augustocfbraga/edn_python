import string

def verificar_palindromo():
    entrada = input("Digite a palavra ou frase: ")
    
    # 1. Deixa tudo em minúsculo
    texto = entrada.lower()
    
    # 2. Remove espaços e pontuações usando a biblioteca string
    # Mantém apenas letras e números
    texto_limpo = "".join(char for char in texto if char.isalnum())
    
    # 3. Compara com a versão invertida
    if texto_limpo == texto_limpo[::-1]:
        print("Sim")
    else:
        print("Não")

if __name__ == "__main__":
    verificar_palindromo() #apresentacao
