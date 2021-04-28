print('\033[;32m-=-\033[m'*23)
print('Me dê o tamanho de \033[0;34mtrês\033[m retas e digo se é possível formar um triângulo')
print('\033[;32m-=-\033[m'*23)
r1 = float(input('Primeiro valor: '))
r2 = float(input('Segundo valor: '))
r3 = float(input('Terceiro Valor: \33[m'))

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('Com estes numeros \33[4mé possível formar\33[m um triangulo')
else:
    print('Com estes números \33[4mnão é possível\33[m formar triangulo')
