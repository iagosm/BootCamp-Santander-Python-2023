contatos = {
  "guilherme@gmail.com": {"nome": "Iago Sousa", "idade": 32, "profissao": "Desenvolvedor"},
  "matheus@gmail.com": {"nome": "Matheus Sousa", "idade": 32, "profissao": "Desenvolvedor"},
  "deivid@gmail.com": {"nome": "Deivd Sousa", "idade": 32, "profissao": "Desenvolvedor"}
}

idade = contatos["deivid@gmail.com"]["idade"]
print(idade)

# for chave in contatos: 
  # print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)