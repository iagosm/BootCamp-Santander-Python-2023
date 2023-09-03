contatos = {
  "guilherme@gmail.com": {"nome": "Iago Sousa", "idade": 32, "profissao": "Desenvolvedor"}
}

contatos.update({"guilherme@gmail.com": {"Iago": "teste"}}) # {'guilherme@gmail.com': {'Iago': 'teste'}}
print(contatos)
