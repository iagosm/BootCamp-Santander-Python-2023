contatos = {
  "guilherme@gmail.com": {"nome": "Iago Sousa", "idade": 32, "profissao": "Desenvolvedor"}
}

# contatos["chave"] # KeyError

resultado = contatos.get("chave") # none
print(resultado)

resultado = contatos.get("chave", []) # []
print(resultado)
 
resultado = contatos.get("guilherme@gmail.com", []) # {"nome": "Iago Sousa", "idade": 32, "profissao": "Desenvolvedor"}
print(resultado)
 