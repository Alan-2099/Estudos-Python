from time import sleep
from math import pow

peso = float(input('Informe seu peso '))
altura = float(input('Informe sua altura '))
print('Vou calcular seu IMC...')
sleep(1)
imc = peso / pow(altura, 2)
if imc <= 18.5:
    print('{:.2f}, seu IMC está abaixo do recomendado'.format(imc))
elif imc > 18.6 and imc <= 25:
    print('{:.2f}, seu IMC está no ideal!'.format(imc))
elif imc > 25.1 and imc <= 30:
    print('{:.2f}, seu IMC indica que você está com sobrepeso'.format(imc))
elif imc > 30.1 and imc <= 40:
    print('{:.2f}, seu IMC está muito elevado (Obesidade)')
else:
    print('{:.2f}, seu IMC está indicado obesidade mórbida'.format(imc))