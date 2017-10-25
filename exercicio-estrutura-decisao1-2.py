nota1 = int(input('Digite a primeira nota:\n'))
nota2 = int(input('Digite a segunda nota:\n'))

media = (nota1 + nota2) / 2

if media < 6:
    print('Média:',media,'- Reprovado!')
else:
    print('Média:',media,'- Aprovado!')