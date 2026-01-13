def validar_senha():
    print("--- Verificador de Segurança de Senha 2026 ---")
    senha = input("Digite a senha para validar: ")

    # Critério A: Comprimento
    tem_tamanho = len(senha) >= 8

    # Critério B: Pelo menos um número
    tem_numero = any(char.isdigit() for char in senha)

    print("\nAnálise:")
    
    if tem_tamanho and tem_numero:
        print("✅ Senha segura! Atende a todos os requisitos.")
    else:
        print("❌ Senha insegura. Motivos:")
        if not tem_tamanho:
            print("- Deve ter pelo menos 8 caracteres.")
        if not tem_numero:
            print("- Deve conter pelo menos um número.")

if __name__ == "__main__":
    validar_senha()
