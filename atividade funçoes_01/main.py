# Declaração da funções

import math

def equacao_primeiro_grau(a, b):
    if a == 0:
        return "A equação não é de primeiro grau."
    return f"A solução da equação é x = {-b / a}"

def equacao_segundo_grau(a, b, c):
    if a == 0:
        return "A equação não é de segundo grau."
    
    delta = b**2 - 4*a*c
    if delta < 0:
        return "A equação não possui raízes reais."
    elif delta == 0:
        x = -b / (2*a)
        return f"A equação possui uma raiz real: x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"As raízes da equação são x1 = {x1} e x2 = {x2}"
    
while True:
    print("\nEscolha uma opção:")
    print("1 - Resolver equação do 1º grau (ax + b = 0)")
    print("2 - Resolver equação do 2º grau (ax² + bx + c = 0)")
    print("3 - Sair")
    
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        print(equacao_primeiro_grau(a, b))
    elif opcao == "2":
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        c = float(input("Digite o coeficiente c: "))
        print(equacao_segundo_grau(a, b, c))
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente!")
    

    
    



        

    



