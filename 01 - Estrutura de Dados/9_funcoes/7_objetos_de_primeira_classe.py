def somar(a, b):
  return a + b

def subtrair(a, b):
  return a - b

def test(a, b):
  return a*2 + b*3

def exibir_resultado(a, b, funcao):
  resultado = funcao(a, b)
  print(f"O resultado da operação é igual a {resultado}")


exibir_resultado(12, 12, somar)
exibir_resultado(12, 12, subtrair)
exibir_resultado(12, 12, test)