def exibir_poemas(data_extensao, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extensao}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


print(exibir_poemas(
    "Segunda, 04 de setembro de 2023",
    "Rosas são vermelhas",
    "Imagina se tivesse uma arma de verdade",
    "Uma flor a desabrochar",
    "Antes, e com tal zelo, e sempre, e tanto",
    "E assim, quando mais tarde me procure",
    "Que não seja imortal, posto que é chama", 
    "Autor Iago"
))

print(exibir_poemas("Segunda, 4 de novembro de 2023", "Testando o poema", autor="Iago", ano=2000))
