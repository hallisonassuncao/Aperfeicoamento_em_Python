# declaração de função
def calcular_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# algoritmo principal
try: 
    B = float(input('Informe o valor da base: ')replace(',', '.'))
    H = float(input('Informe o valor da altura: ').replace(',', '.'))
    area = calcular_triangulo(B, H)

    print(f'A área do triângulo é: {area}')
except Exception as e:
    print(f'Não foi possivel calcular a area do triangulo: {e}')   
