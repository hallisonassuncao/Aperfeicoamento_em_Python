import os

# Configuração das mensagens do commit
commit_message = "Atualização automática do projeto"

# Caminho do repositório local
repo_path = r"C:\caminho\para\seu\repositorio"

# Navegar até o repositório
os.chdir(repo_path)

# Adicionar todos os arquivos ao commit
os.system("git add .")

# Criar o commit
os.system(f'git commit -m "{commit_message}"')

# Enviar o commit para o GitHub
os.system("git push origin main")

print("Commit e push realizados com sucesso!")
