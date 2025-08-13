dados = []

x = 1
while x != 3:
    print("O que deseja fazer?\n1 - Lançar notas\n2 - Ver notas lançadas\n3 - Sair") 
    x = int(input("Resposta: "))

    if x == 1:
        id_aluno = input("Nome do aluno: ")
        ra_aluno = input("RA do aluno: ")
        nota1 = float(input("Digite a nota da Av1: "))
        nota2 = float(input("Digite a nota da Av2: "))
        media = (nota1 + nota2) / 2

        aluno = {
            "nome": id_aluno,
            "ra": ra_aluno,
            "media": media
        }

        dados.append(aluno)

        if 6 < media <= 10:
            status = "Aprovado"
        elif 5 <= media <= 6:
            status = "Recuperação"
        elif 0 <= media < 5:
            status = "Reprovado"
        else:
            status = "Nota inválida, tente novamente."

        print(f"Nota final: {media:.2f} - {status}")
        print("__________________________\n")

    elif x == 2:
        if dados:
            print("Notas lançadas:")
            for i, aluno in enumerate(dados, 1):
                print(f"{i} - Nome: {aluno['nome']}, RA: {aluno['ra']}, Nota final: {aluno['media']:.2f}")
        else:
            print("Nenhuma nota lançada ainda.")
        print("__________________________\n")

    elif x == 3:
        print("Saindo do programa...")

    else:
        print("Opção inválida. Tente novamente.")