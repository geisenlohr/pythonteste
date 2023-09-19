nome = str(input('Qual é o seu nome? '))
if nome == 'Guilherme':
    print('Que nome bonito!')

elif nome == 'Pedro' or nome == 'Pedro' or nome == 'Paulo':
    print('Que nome comum!')

elif nome in 'Ana Claudia Juliana Andrea':
    print('Belo nome feminino!!!')

else:
    print('Que nome feio!')

print('Tenha um bom dia, {}'.format(nome))


