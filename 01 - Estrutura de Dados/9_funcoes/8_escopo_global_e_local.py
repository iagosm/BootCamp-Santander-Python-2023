salario = 2000

def salario_bonus(bonus, lista):
  global salario # sem essa parte ele da erro por acabar não puxando o salario
  lista_aux = lista.copy()
  lista_aux.append(2)
  print(f"lista aux = {lista_aux}")
  salario += bonus
  return salario

lista = [1]
salario_bonus(500) # 2500
lista_auxu = salario_bonus(500, lista) # 2500
print(lista_auxu)