
# tratamento de exceções
while True:
    try:
        # declaração de variáveis
        nome = input("Informe seu nome: ")
        idade = int(input("Informe sua idade: "))

        # saída de dados
        print(nome, "é maior de idade" if idade >= 18 else "não é maior de idade.")

        # decisão
        continuar = input("Deseja continuar? (s/n): ")

        match continuar:
            case 's':
                continue
            case 'n':
                break
            case _:
                print("nao foi possivel computar sua decisao")
                continue
    except Exception as e:
        print(f"dados informados invalidos: {e}")
        continue
    
    
            