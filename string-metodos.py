palavra = 'maintenance informática'

print('-Tamanho:', len(palavra))
print('-Primeira letra maiúscula:', palavra.capitalize())
print('-Conta caractere:', palavra.count('n'))
print('-Converte para maiúscula:', palavra.upper())
print('-Verifica se todas são maiúsculas:', palavra.isupper())
print('-Inverte o conteúdo da string:', palavra.swapcase())
print('-Converte para maiúsculo cada palavra:', palavra.title())
print('-Transforma a string em lista:', palavra.split())
print('-Substitui trecho S1 pelo S2:', palavra.replace('informática', 'eletrônica'))
print('-Remove espaços direitos da string:', palavra.rstrip())

print('-Fatiamento de string: ', palavra[1:4])
print('-Fatiamento de string: ', palavra[4:])
print('-Fatiamento de string: ', palavra[:4])

