contador = 0
soma = 0
while contador < 3:
    contador += 1
    notas = float(input('Digite a '+str(contador)+'ª nota: '))
    soma += notas
    media = soma / contador
print('Média =', media)