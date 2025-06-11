# Importar biblioteca
import os

# Declaração de lista
nomes = ["Fulano", "Ciclano", "Belatrano", "João", "Maria", "Jose"]

# Tratamento de Exceção
try:
    # Loop infinito
    while True:
        # Limpar terminal
        os.system("cls")  
        
        # Exibir a lista
        for i in range(len(nomes)):
            print(f"Nome de código {i}: {nomes[i]}.")
        
        # Solicitar ao usuário a opção desejada
        opcao = input("Escolha uma opção: (e) Excluir, (n) Sair: ").lower()
        
        match opcao:
            case "e":
                posicao = int(input("Informe o código do nome a ser excluído: "))  
                if 0 <= posicao < len(nomes): 
                    del nomes[posicao]
                    os.system("cls")
                    print("Item excluído com sucesso!\n")
                else:
                    print("Código inválido! Tente novamente.")
                continue
            case "n":
                print("Encerrando o programa.")
                break
            case _:
                print("Opção inválida!")
                continue

except Exception as e:
    print(f"Não foi possível executar a ação. Erro: {e}.")
