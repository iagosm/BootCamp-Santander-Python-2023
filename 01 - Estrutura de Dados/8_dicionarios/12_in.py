contatos = {
  "guilherme@gmail.com": {"nome": "Iago Sousa", "idade": 32, "profissao": "Desenvolvedor"},
  "matheus@gmail.com": {"nome": "Matheus Sousa", "idade": 32, "profissao": "Desenvolvedor"},
  "deivid@gmail.com": {"nome": "Deivd Sousa", "idade": 32, "profissao": "Desenvolvedor"}
}

# Verificação se existe ou não no dicionario

resultado = "idade" in contatos["guilherme@gmail.com"] # True
print(resultado)

resultado = "abatataPalhagmail.com" in contatos # False
print(resultado)

resultado = "telefone" in contatos["matheus@gmail.com"] # False
print(resultado)