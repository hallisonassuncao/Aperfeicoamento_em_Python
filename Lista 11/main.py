# NOTE  o SPLIT separe os valores de uma variavel em uma lista

# variaveis
ano = "Jan, Fev, Mar, Abr, Mai, Jun, Jul, Ago, Set, Out, Nov, Dez"

# Algaritmo
try:
    meses = ano.split(",")
    for mes in meses:
        print(mes)
except Exception as e:
    print(f"Não foi possivel separar os valores.{e}.")

