from time import sleep

km = float(input('Qual o km que o condutor estava? '))
print('deixe-me analisar aqui...')
sleep(1)
if km > 80:
    multa = (km * 7) - 560
    print('Velocidade acima de \33[33m80km\33[m por hora!\nO infrator passou a \33[33m{}km\33[m, receberá uma multa no valor de R${:.2f}'.format(km, multa))
else:
    print('Velocidade permitida, tenha um bom dia.')
sleep(5)
