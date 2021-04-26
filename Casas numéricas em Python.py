from time import sleep
frase=int(input('Digite um número: '))
u= frase // 1 % 10
d= frase // 10 % 10
c= frase // 100 % 10
m= frase // 1000 % 10
print('Unidade {}'.format(u))
print('Centena {}'.format(d))
print('Dezena {}'.format(c))
print('Milhar {}'.format(m))

sleep(4)
