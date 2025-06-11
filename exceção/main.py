
# Tratamento de Exceções
try:
    # Declaração de variáveis
    x = int(input("Informe um número inteiro:"))

    # Saída de Dados
    print(f"O número informado foi {x}.")
except Exception as e:
    print(f"Não foi possível ler o número informado pelo usuário. Erro: {e}")
finally:
    print("Meu Programa foi executado com sucesso.")