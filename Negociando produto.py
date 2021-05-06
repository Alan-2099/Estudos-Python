valor = float(input('Qual o valor do produto? '))
fpag = int(input('Como será a forma de pagamento? \n(Dinheiro ou Cheque [1] (à vista), no crédito [2] (opções de parcelamento) '))
desc10 = valor - (valor * 0.10)
desc5 = valor - (valor * 0.05)
juros = valor + (valor * 0.20)
if fpag <= 1:
    print('O valor a ser pago terá um desconto de 10%, então será de ${:.2f}'.format(desc10))
elif fpag == 2:
    print('Caso não vá parcelar, o produto terá um desconto de 5%, ficando ${:.2f}'.format(desc5))
    parcela = int(input('O produto será parcelado? [1] sim [2] não: '))
    if parcela == 1:
        vezes=int(input('Você optou por parcelar, o produto será parcelado em quantas vezes? '))
        if vezes <= 1:
            print('O produto não será parcelado, ganhando o desconto de 5%, ficando {:.2f}'.format(desc5))
        elif vezes == 2:
            print('O produto não terá alteração de valor, permanecendo ${:.2f}'.format(valor))
        elif vezes > 2:
            print('O valor a ser pago terá um acréssimo de juros de 20%, ficando {:.2f}'.format(juros))
            print('Cada parcela será de ${:.2f}'.format(juros / vezes))
        else:
            print('Opção inválida, repita o processo')
    elif parcela == 2:
        print('O produto não será parcelado, ganhando o desconto de 5%, ficando {:.2f}'.format(desc5))
    else:
        print('Opção inválida, repita o processo')
else:
    print('Opção inválida, repita o processo')
