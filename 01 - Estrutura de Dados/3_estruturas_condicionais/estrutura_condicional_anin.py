CONTA_NORMAL = True
CONTA_UNIVERSITARIA = False
saldo = 2000
saque = 500 
cheque_especial = 450

if CONTA_NORMAL:
    if saldo >= saque:
        print('Saque realizado com sucesso')
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print('Não foi possivel realizar o saque')
elif CONTA_UNIVERSITARIA :
    if saldo >= saque:
        print('Saque realizado com sucesso')
else:
    print('Sistema não reconheceu o tipo de conta, entre em contato com o gerente.')      