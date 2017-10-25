valor = int(input('Qual sua idade?\n'))

if valor < 6:
    print('Que coisa fofa!')
elif valor < 18:
    print('Você ainda não pode dirigir!')
elif valor > 60:
    print('Você está na melhor idade!')
else:
    print('Você é o cara!')