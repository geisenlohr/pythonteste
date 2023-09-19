'''
# 1ª Situação
for c in range(1,10):
    passo                            # está dentro do laço
pega                                 # está fora do laço

# 2ª Situação
for c in range(0,3):
    passo
    pula                             # está dentro do laço
passo
pega                                 # está fora do laço

# 3ª Situação
for c in range(0,3):
    if coin:
        pega
    passo
    pula
passo
pega


for c in range(0, 16, 2):
    print(c)
print('Fim!')


i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim do programa!')
'''
s = 0
for c in range(0,3):
    n = int(input('Digite um valor: '))
    s = s + n                  # ou       s += n
print('A soma de todos os valores foi {}'.format(s))
