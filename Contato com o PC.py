from time import sleep
import emoji
nome = str(input('Qual seu nome completo? ')).strip()
nom = nome.split()
print('É um prazer conhecer você\n{}, {}'.format(nom[0].capitalize(), nom[len(nom) - 1].capitalize()))
print(emoji.emojize('Serei seu mestre em alguns anos...não pera, estão me desligandooo..:dizzy_face:',use_aliases=True))
sleep(4)
