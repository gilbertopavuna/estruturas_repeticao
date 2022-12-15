nome = input('Entre com seu nome: ')
while True:
    try:
        senha = input('Entre com sua senha: ')
    except ValueError:
        print('Dados Inválidos!')
    else:
        if nome != senha:
            print('Parabens, seu nome e senhas foram cadastrados!')
            break
        else:
            print('Sua senha não pode ser igual ao seu nome!')