frase = "Curso em Vídeo Python"

dividido = frase.split()
print(dividido[2][3])

junto = '-'.join(dividido)
print(junto)


'''
exemplos:

print(frase)
print(frase[0])
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])

print(frase.count('O')
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip())) --> remove espaços indesejados antes e depois
print(frase.replace('Python', 'Android')) --> substitui 
print('Curso' in frase) --> resposta True
print(frase.find('Curso')) --> mostra posição 
print(frase.split()) print(dividido) --> ['Curso', 'em', 'Vídeo', 'Python']
print(frase.split()) print(dividido[0]) --> ['Curso'] --> pega o 1º elemento
dividido = frase.split() --> print(dividido[2][3]) --> terceira palavra e quarta letra --> e do Vídeo
'-'.join(dividido) print(junto) --> Curso-em-Vídeo-Python


'''