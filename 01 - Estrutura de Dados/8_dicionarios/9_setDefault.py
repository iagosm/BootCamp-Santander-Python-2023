contato = {'nome': 'Iago', 'telefone': '1321-3131'}

contato.setdefault("nome", "José") #iago
print(contato)

contato.setdefault("idade", "29") # idade: 29
print(contato)

# Caso já exista, ele não faz nada, se não existir ele cria.