#Tratamento de exceções
try:
    #declaração de variáveis
    n = int(input("Informe um numero inteiro positivo: "))

    #loop
    while n >= 0:
        print(n)
        n -= 1  

except Exception as e:
    print(f"numero invalido.{e}")
