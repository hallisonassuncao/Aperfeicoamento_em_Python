# dicionario
usuario = dict(nome="Fulano de tal", idade=18, email="fulano@gmail.com")

# exibindo os dados de dicionario
for chave in usuario:
    print(f"{chave.title()}:{usuario.get(chave)}.")