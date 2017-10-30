import random

numero = random.randint(1,100)

escolha, tentativas = 0, 0
while escolha != numero:
    escolha = int(input('- Escolha um número entre 1 e 100:\n'))
    tentativas += 1
    if escolha < numero:
        print('\nO número', escolha, 'é menor que o sorteado.')
    elif escolha > numero:
        print('O número', escolha, 'é maior que o sorteado.')
print('Parabéns! Você acertou com', tentativas, 'tentativas.')