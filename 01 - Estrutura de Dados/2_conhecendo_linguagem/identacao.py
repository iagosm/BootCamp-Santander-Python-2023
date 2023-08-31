def sacar(valor):
    saldo = 100
    if saldo >= valor:
        print('Valor sacado')
        print('Retire o seu dinheiro no caixa')
    print('Obrigado por ser nosso cliente, tenha um ótimo dia!')

sacar(200)

def depositar(valor):
    saldo = 500
    saldo += valor