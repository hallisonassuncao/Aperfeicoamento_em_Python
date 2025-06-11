# Criar uma lista de Compras
def ordenar_lista_compras():
    print("Digite os itens da sua lista de compras.")
    print("Digite 'fim' para encerrar a entrada.")

    lista_compras = ["Miojo","Alho", "Feijão", "Macarrão", "Carne", "Frango"]

    while True:
        item = input("Insira um item da lista: ")
        if item.lower() == 'fim':
            break
        lista_compras.append(item)

    lista_compras.sort()

    print("\nSua lista de compras em ordem alfabética:")
    for item in lista_compras:
        print(item)

# Execute
ordenar_lista_compras()


    



