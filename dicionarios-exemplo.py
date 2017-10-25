d = {
    'arroz': 17.30,
    'feijão': 12.50,
    'carne': 23.90,
    'alface': 3.40
}
print(d)

print('\n', d['carne'])

print('\nVerificar existência de chave')
print('carne' in d)

print('\nExibir as chaves do dicionário')
print(d.keys())

print('\nExibir os valores do dicionário')
print(d.values())

print('Operações em dicionários:\n')
print('Remover elemento feijão')
d.pop('feijão')
print(d)