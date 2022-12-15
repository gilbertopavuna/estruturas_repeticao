while True:
    try:
        nota = int(input('Entre com sua nota: '))
    except ValueError:
        print('Digite um valor inteiro')
    else:
        if 0 <= nota <= 10:
            print(f'Sua nota é {nota}.')
            break
        else:
            print('Digite um valor de 0 a 10.')
