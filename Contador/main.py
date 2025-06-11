# tratamento de exceção

try:
    # declaração de variável
    n = int(input(' informe o numero inteiro positivo:'))

    # laço for
    for i in range(n+1):
        print(i) 

except Exception as e:
     print(f' não foi possivel realizar a contagem. {e}.')

# tratamento
    
    
    
    
