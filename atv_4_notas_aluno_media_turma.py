def sistema_notas():
    turma = {}
    print("--- Registro de Notas 2026 ---")

    while True:
        nome = input("\nNome do aluno (ou 'fim' para calcular): ").strip()
        if nome.lower() == 'fim':
            break
        
        try:
            nota = float(input(f"Nota de {nome}: "))
            if 0 <= nota <= 10:
                turma[nome] = nota
            else:
                print("Erro: A nota deve ser entre 0 e 10.")
        except ValueError:
            print("Erro: Insira um valor numérico para a nota.")

    if turma:
        print("\n--- Relatório Final ---")
        for aluno, nota in turma.items():
            print(f"Aluno: {aluno:<15} | Nota: {nota:>5.1f}")
        
        media_turma = sum(turma.values()) / len(turma)
        print("-" * 36)
        print(f"Média Geral da Turma: {media_turma:.2f}")
        print(f"Total de alunos: {len(turma)}")
    else:
        print("Nenhum dado foi inserido.")

if __name__ == "__main__":
    sistema_notas()
