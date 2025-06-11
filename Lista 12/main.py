import os

nomes = ["Fulano", "Ciclano", "Beltrano", "Joçao", "Maria", "José"]

try:
    while nomes:  
        for i in range(len(nomes)):
            print(f"Código {i}: {nomes[i]}")
        
        posição = int(input("Informe o código do item a ser separado: "))
        
        if posição < 0 or posição >= len(nomes):
            print("Código inválido. Tente novamente.")
            continue
        
        nome_separado = nomes.pop(posição)  # Separa o item da lista
        os.system("cls" if os.name == "nt" else "clear") 
        print(f"Item separado: {nome_separado}")
    
    print("Todos os itens foram separados!")
except Exception as e:
    print(f"Não foi possível separar o item da lista.{e}.")
