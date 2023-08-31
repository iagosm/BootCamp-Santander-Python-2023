nome = 'Iago'
idade = 28
profissao = 'Desenvolvedor'
linguagem = 'Python'
saldo = 43.923
dados = {"nome": "Iago Sousa", "idade": 23}


print('Nome: %s Idade: %d' % (nome, idade))
print('Nome: {1} Idade: {0}'.format(idade, nome))
print('Nome: {idade} Idade: {nome}'.format(nome= nome, idade = idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome}, Idade: {idade}")
print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo:.2f}")