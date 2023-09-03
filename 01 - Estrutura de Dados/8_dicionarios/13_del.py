contatos = {
  "guilherme@gmail.com": {"nome": "Iago Sousa", "idade": 32, "profissao": "Desenvolvedor"},
  "matheus@gmail.com": {"nome": "Matheus Sousa", "idade": 32, "profissao": "Desenvolvedor"},
  "deivid@gmail.com": {"nome": "Deivd Sousa", "idade": 32, "profissao": "Desenvolvedor"}
}

del contatos["matheus@gmail.com"]["profissao"]
del contatos["deivid@gmail.com"]
print(contatos)