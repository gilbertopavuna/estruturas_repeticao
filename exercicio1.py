try:
    nota = float(input('Entre com sua nota: '))
except ValueError:
    print('Digite um valor de 0 a 10.')
else:
    print(f'Sua nota é {nota}.')