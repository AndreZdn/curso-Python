from datetime import date

ano = int(input('digita um ano ai meu chapa, coloque zero para analisar o ano atual:  '))

if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%100 != 0 or ano % 400 == 0:
    print('esse ano de {} é um ano bissexto'.format(ano))
else:
    print('esse ano de {} não é um ano bissexto'.format(ano))