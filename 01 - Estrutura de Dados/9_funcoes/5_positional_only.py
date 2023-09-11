def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): # os parametros após a barra podemos passar nomeados ou não
  print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1923", marca="Fiat", motor="1.5v", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1923", marca="Fiat", 
            motor="1.5v", combustivel="Gasolina") # Esse vai dar erro, por que não pode adicionar a posição.


