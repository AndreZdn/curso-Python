somaidade = 0
hvelho = 0

contadormulher = 0
for c in range(0, 4):
    nome = str(input('Qual é o seu nome?'))
    idade = int(input('qual é a sua idade'))
    sexo = int(input('''Voce é homem ou mulher?
    [1]HOMEM
    [2]MULHER
    Digite sua resposta'''))
    somaidade += idade
    if sexo == 1 and idade >= hvelho:
        hvelho = idade
        # o h siginifica que a variavel é pra homem
        hnvelho = nome
        # hn é Homem e nome e o mair
    if sexo == 2 and idade < 20:
        contadormulher += 1
    print('fim dos dados da {}° pessoa'.format(c+1))
print('nessa lista de pessoas a media de idade foi de {}'.format(somaidade/4))
print('o homem mais velho foi {} com {} anos'.format(hnvelho, hvelho))
print('nessa lista teve o total de {} mulheres com menos de 20 anos'.format(contadormulher))
        

