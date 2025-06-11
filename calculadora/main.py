#declaração de variaveis
x = float(input( "informe o valor de x: "))
y = float(input( "informe o valor de y: "))

#mostrar o menu
print("escolha a operação desejada:")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")
print("5 - resto da divisão")

#usuário escolhe a operação
operador = int(input("informe a operação desejada: "))

# estrutura match
match operador:
    case "1":
        print(f"resultado da soma: {x+y}")
    case "2":
        print(f"resultado da subtração: {x-y}")
    case "3":
        print(f"resultado da multiplicação: {x*y}")
    case "4":
        print(f"resultado da divisão: {x/y}")
    case "5":
        print(f"resto da divisão: {x%y}") 
    case _:
        print("operador invalido")
        



        



