MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade: "))
if(idade >= 18):
    print('Maior de idade, pode tirar a CNH')
if idade < MAIOR_IDADE:
    print('Ainda não pode tirar a CNH')
    

idade = int(input("Informe sua idade: "))
if(idade >= 18):
    print('Maior de idade, pode tirar a CNH')
elif idade == IDADE_ESPECIAL:
    print('Pode fazer as aulas teóricas, porém ainda não está disponivél para verificar e realizar as aulas práticas.')
if idade < MAIOR_IDADE:
    print('Ainda não pode tirar a CNH')