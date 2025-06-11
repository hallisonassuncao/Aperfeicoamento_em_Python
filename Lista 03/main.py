import os

# Declaração da lista
lista = []

# Tratamento de exceção
try:
    # Loop infinito 
    while True:
        # Input
        item = input("Informe o nome do item ou deixe em branco para encerrar: ")
        
        # Limpa o terminal
        os.system("cls" if os.name == "nt" else "clear")  # limpa o terminal
        
        # Verificar se o item está vazio ou não
        if item != "":
            lista.append(item)  # Adiciona o item à lista
            print(f"{item} inserido na lista com sucesso")
            continue         
        else:
            break 

    # Ordena a lista
    lista.sort()

except Exception as e:
    print(f"não foi possível inserir item na lista. Erro: {e}.")
finally:
    print("Lista de itens:")
    for i in lista:
        print(item)

        

        # Declaração de lista
lista = ["Maça", "Uva", "Laranja", "Morango", "Manga"]

# Ordenando a lista em ordem alfabética
lista.sort()

# Exibindo os itens ordenados
for fruta in lista:
    print(fruta)

    


        


   

 
     
     