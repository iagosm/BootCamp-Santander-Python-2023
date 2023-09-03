pessoa = {"nome": "Guilherme", "idade" : 32}


pessoa = dict(nome="Guilherme", idade=32) # {'nome': 'Guilherme', 'idade': 32}
print(pessoa)
pessoa["telefone"] = "3333-1234" # {'nome': 'Guilherme', 'idade': 32, 'telefone': '3333-1234'}
print(pessoa)


dados = {"nome": "Guilherme", "idade" : 32, "telefone": "3214-3123"}

dados['nome'] # "Guilherme"
dados['idade'] # 32 
dados['telefone'] # "3214-3123"


dados['nome'] = 'Iago Sousa'
dados['idade'] = 23
dados['telefone'] = '9999-9999'
print(dados)