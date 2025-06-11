#declaração de função
def dar_boas_vindas(nome,curso):
    return f'Olá {nome}, seja bem-vindo ao curso de {curso}'

# algoritmo principal
nome = input('Digite seu nome: ')
curso = input('Digite o nome do curso: ')

print(dar_boas_vindas(nome, curso)) 