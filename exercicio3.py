nome = input('Entre com seu nome: ')  # nome > 3 caracteres
idade = int(input('Entre com sua idade: '))  # idade entre 0 e 150
salario = float(input('Entre com seu salário: '))  # salario maior que 0
sexo = input('Entre com M- masculino ou F- feminino: ').upper()
estado_civil = input('Entre com S- solteiro, C- casado, V- viúvo ou D- divorciado: ').upper()

while True:
    if len(nome) < 4:
        nome = f'Erro: o nome precisa ter 3 letras ou mais, não pode ser {nome}'
        print(nome)
    if 0 < idade > 150:
        idade = f'Erro: a idade precisa estar entre 0 e 150, não pode ser {idade}'
        print(idade)
    if salario <= 0:
        salario = f'Erro: o salário precisa ser positivo, não pode ser {salario}'
        print(salario)
    if sexo != 'M' and sexo != 'F':
        sexo = f'Erro: o sexo precisa ser "M" ou "F", não pode ser {sexo}'
        print(sexo)
    if estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
        estado_civil = f'Erro: o estado civil precisa ser "S", "C", "V" ou "D", não pode ser {estado_civil}'
        print(estado_civil)
        break
    else:
        print('Cadastro realizado com sucesso!')
        break