contatos = {
  "guilherme@gmail.com": {"nome": "Iago Sousa", "idade": 32, "profissao": "Desenvolvedor"},
  "matheus@gmail.com": {"nome": "Matheus Sousa", "idade": 32, "profissao": "Desenvolvedor"},
  "deivid@gmail.com": {"nome": "Deivd Sousa", "idade": 32, "profissao": "Desenvolvedor"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Erick", "idade":22}
print(copia)