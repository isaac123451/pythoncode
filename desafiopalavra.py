import os

palavra_secret = input('Digite a palavra para o jogo: ')
letra_acertadas = ''
tentativas = 0

while len(palavra_secret) > 1:
    palavra_formada = ''
    letra_digit = input('Digite uma letra: ')
    tentativas += 1
    if len(letra_digit) > 1:
        print('Digite apenas uma letra.')
        continue
    if letra_digit in palavra_secret:
        letra_acertadas += letra_digit

    for letra_secreta in palavra_secret:
        if letra_secreta in letra_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secret:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secret)
        print('Tentativas:',tentativas)
        letras_acertadas = ''
        tentativas = 0
