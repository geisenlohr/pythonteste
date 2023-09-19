# Cores no terminal

# letra branca fundo vermelho \033[0;97;41m

# sublinhado letra amarela fundo azul \033[4;33;44m

# negrito letra magenta fundo amarelo \033[1;35;43m

# letra branca fundo verde \033[97;42m

# letra cinza fundo preto \033[m ---> serve para fechar configuração

# ex.: print('\033[1;31;43mOlá, Mundo!!!\033[m')

# letra preta fundo cinza \033[7;30m

nome = 'Guilherme'
print('Olá, {}, prazer em conhecer você.'.format('\033[0;34m', nome, '\033[m'))



