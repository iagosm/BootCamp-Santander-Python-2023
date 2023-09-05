def calcular_total(numeros):
  return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
  antecessor = numero - 1
  sucessor = numero + 1

  return antecessor, sucessor

def func_3():
  print('Olá mundo')
  # return 42

print(calcular_total([12, 30, 90])) # 132 
print(retorna_antecessor_e_sucessor(10)) # 9 , 11 
print(func_3())