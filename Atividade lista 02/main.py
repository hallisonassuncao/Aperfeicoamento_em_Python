
# Crie um programa em que o usuario informa varias notas de um aluno de 0 a 10 ( quantas notas ele quiser inserir) , e ao final , o programa calcule a media
# desse aluno e informe se ele esta aprovado, de recuperação ou reprovado.

#Obs: medias para aprovação: 7 , media para recuperação : entre 5 e 6. abaixo de 5 : reprovado

numero_decimal = float(input("Informe um numero decimal:").replace(",","."))
print(f"{numero_decimal} -{type(numero_decimal)}")


# Programa para calcular a média do aluno e determinar sua situação
notas = []

print("Insira as notas do aluno (digite -1 para finalizar):")

while True:
    try:
        nota = float(input("Informe a nota do aluno: ").replace(",", "."))
        if 0 <= nota <= 10:  
            notas.append(nota) 
            print("Nota inserida com sucesso")
        elif nota == -1:
            break
        else:
            print("Nota inválida. Insira um valor entre 0 e 10 ou -1 para finalizar.")
            continue
        
        continuar = input("Deseja inserir outra nota? (s/n):")
        if continuar == "s":
            continue
        elif continuar == "n":
            break
        else:
            print("Opção inválida. Por favor, responda com 's' ou 'n'.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")


    else:
        print("Nota invalida. Favor inserir uma nota valida.")
        continue
    for i in range(len)(notas)
except Exception as e:

finally:

print(f"Media das notas: {media}.")

if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia do aluno: {media:.2f}")

    if media >= 7:
        print("Situação: Aprovado")
    elif 5 <= media < 7:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")
else:
    print("\nNenhuma nota foi inserida.")


        



