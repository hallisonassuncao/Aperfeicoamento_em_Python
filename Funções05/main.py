from funcoes import calcular_quadrilatero, calcular_triangulo

def obter_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

if __name__ == "__main__":
    try:
        print("Escolha a figura da qual deseja calcular a área:\n")
        print("1 - Quadrilátero")
        print("2 - Triângulo")
        opcao = input("Digite o número da figura desejada: ")

        if opcao in ["1", "2"]:
            base = obter_valor("Informe o valor da base: ")
            altura = obter_valor("Informe o valor da altura: ")

            match opcao:
                case "1":
                    print(f"Resultado: {calcular_quadrilatero(base, altura)}")
                case "2":
                    print(f"Resultado: {calcular_triangulo(base, altura)}")
        else:
            print("Opção inválida. Tente novamente.")

    except Exception as e:
        print(f"Não foi possível calcular a área devido a um erro inesperado: {e}")