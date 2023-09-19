'''nome = str(input('Qual é seu nome? '))

if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Nome normal, né?!')
print('Bom dia, {}!'.format(nome))'''

'''n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))

m = (n1 + n2)/2

print('A sua média foi {:.1f}'.format(m))

if m >= 6:
    print('Boa média! Parabéns!')
else:
    print('Média ruim! Precisa estudar mais...')'''


n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))

m = (n1 + n2)/2

print('A sua média foi {:.1f}'.format(m))

print('PARABÉNS!' if m >= 6 else 'Média ruim! Precisa estudar mais...')