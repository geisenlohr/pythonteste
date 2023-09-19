'''cont = 1

while cont <= 10:
    print(cont, '... ', end='')
    cont += 1
print('Acabou!')'''

'''n = cont = 0
while n != 999:
    n = int(input('Digite um nº: '))
print('Fim!')'''

'''n = cont = 0
while cont < 5:
    n = int(input('Digite um nº: '))
    cont += 1
print('Fim!')'''

'''n = s = 0
while n != 999:
    n = int(input('Digite um nº: '))
    s += n
#s -= 999 ----> gambiarra
print('A soma vale {}'.format(s))'''

'''n = s = 0
while True:
    n = int(input('Digite um nº: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}') # ---> interpolação dentro de strings (fstrings) / PEP = program enhancement proposal'''

nome = 'José'
idade = 33
salário = 987.35
print(f'O {nome} tem {idade} anos e ganha R${salário:.2f}.')

# método antigão/Python 2 = print('O %s tem %d anos.' % (nome, idade))

