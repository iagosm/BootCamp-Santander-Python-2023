def exibir_mensagem():
  print('Exibindo a mensagem')

def exibir_mensagem_2(nome):
  print(f"Olá {nome}, sejá bem vindo!")

def exibir_mensagem_3(nome="Anônimo"):
  print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2('Iago')
exibir_mensagem_3()
exibir_mensagem_3('Nome Aleatório')