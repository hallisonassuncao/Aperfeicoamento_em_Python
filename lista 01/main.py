# Declaração da lista
nomes = ["Ana", "Flavio", "Augusto","Paula","Silvia"]

# Tratamento de exceções
try:
    # Loop infinito para entrada de nomes
    while True:
        # Usuário informa o nome
        item = input("Informe um nome ou deixe em branco para exibir a lista: ")

        # Verifica se o nome foi inserido
        if item != "":
            nomes.append(item)
        else:
            break

except Exception as e:
    print(f"Não foi possível inserir dados na lista. Erro: {e}.")

finally:
    # Exibir nomes na ordem alfabética
    nomes.sort()

    print("\nNomes na lista (em ordem alfabética):")
    for nome in nomes:
        print(nome)