numero = int(input('Digite o número para a tabuada:\n'))
for sequencia in range(1,11):
    print('%2d x %2d = %3d' %(sequencia, numero, sequencia*numero))