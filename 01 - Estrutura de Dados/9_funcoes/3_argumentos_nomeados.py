def salvar_carro(marca, modelo, ano, placa):
  print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

print(salvar_carro('Nova Marca', 'Novo Modelo', '2010', 'OZT9123'))
print(salvar_carro(marca="Fiat",modelo="X8JS",ano='2010',placa='OZT9123'))
print(salvar_carro(**{'marca':"Fiat",'modelo':"X8JS",'ano':'2010','placa':'OZT9123'}))
print(salvar_carro(*{'marca':"Fiat",'modelo':"X8JS",'ano':'2010','placa':'OZT9123'}))