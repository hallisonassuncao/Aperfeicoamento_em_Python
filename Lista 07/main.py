# Importar biblioteca
import os

# Declarar a lista
cidades = ["Brasilia", "Rio de Janeiro", "São Paulo", 
           "Belo Horizonte", "Goiania", "Palmas",
           "Brasilia", "Goiania", "Brasilia"]

# Tratamento de exceção
try:
    # Loop infinito
    while True:
        # Limpar o terminal (compatível com Windows)
        os.system("cls") 

        # Usuário informa a cidade a ser pesquisada
        pesquisa = input("Informe a cidade a ser pesquisada: ").title()

        # Retorna a quantidade de vezes que a cidade aparece na lista
        resultado = cidades.count(pesquisa)

        # Mostrar o resultado na tela
        if resultado != 0:
            print(f"{pesquisa} foi encontrada na lista {resultado} vezes.")
        else: 
            print(f"{pesquisa} não foi encontrada na lista.")

        # Pergunta se o usuário deseja realizar uma nova pesquisa
        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            break
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    







    