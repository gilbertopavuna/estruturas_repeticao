try:
    nome = input('Entre com o seu nome: ')
    senha = int(input('Entre com sua senha: '))
except ValueError:
    if senha == nome:
        print('Senha não pode ser igual ao nome.')
else:
    print(f'{nome}, sua senha foi cadastrada.')