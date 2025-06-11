
# Lista para armazenar os cadastros
cadastros = []

def cadastrar():
    pessoa = {
        "Nome": input("Nome:"),
        "CPF": input("CPF:"),
        "E-mail": input("E-mail:"),
        "Telefone": input("Telefone:"),
        "Data de nascimento": input("Data de nascimento (DD/MM/AAAA):"),
        "Gênero": input("Gênero:")
    }
    cadastros.append(pessoa)
    print("Cadastro realizado com sucesso!")

def listar():
    if not cadastros:
        print("Nenhuma pessoa cadastrada.")
        return
    for i, pessoa in enumerate(cadastros, 1):
        print(f"\nCadastro {i}:")
        for chave, valor in pessoa.items():
            print(f"{chave}: {valor}")

def alterar():
    cpf = input("Digite o CPF da pessoa que deseja alterar: ")
    for pessoa in cadastros:
        if pessoa["CPF"] == cpf:
            campo = input("Qual campo deseja alterar? (Nome, E-mail, Telefone, Data de nascimento, Gênero): ")
            if campo in pessoa:
                pessoa[campo] = input(f"Novo valor para {campo}: ")
                print("Dados alterados com sucesso!")
                return
    print("CPF não encontrado!")

def excluir():
    cpf = input("Digite o CPF da pessoa que deseja excluir: ")
    for pessoa in cadastros:
        if pessoa["CPF"] == cpf:
            cadastros.remove(pessoa)
            print("Cadastro excluído com sucesso!")
            return
    print("CPF não encontrado!")

def menu():
    while True:
        opcao = input("\n1 - Cadastrar\n2 - Listar\n3 - Alterar\n4 - Excluir\n5 - Sair\nEscolha uma opção: ")
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            alterar()
        elif opcao == "4":
            excluir()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()



