nota1 = int(input('Digite a primeira nota:\n'))
nota2 = int(input('Digite a segunda nota:\n'))

media = (nota1 + nota2) / 2

if media < 4:
    print('Média:',media,'- Reprovado!')
elif (media >= 4) and (media <= 6):
    print('Média:',media,'- Exame!')
else:
    print('Média:',media,'- Aprovado!')