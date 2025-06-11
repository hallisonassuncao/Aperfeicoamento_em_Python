#declaração de variaveis
nome =input("informe o nome do aluno:!")
nota =float(input("infome a nota do aluno:"))

#verificar se o aluno passou ou não
if nota >= 0 and nota <= 10:
    if nota >= 7:
        print(f"{nome} esta aprovado.")

    elif nota >= 5:
        print (f"({nome} esta em recuperação.")
    else:
        print (f"{nome} esta reprovado.")
