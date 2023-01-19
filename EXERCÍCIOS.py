#Exércício 1#

"""
    Peça ao usuário para digitar o nome e a idade.
    Se forem digitados, exiba:
        'Seu nome é {nome}'
        'Seu nome invertido é {nomeinvertido}'
        Se nome contêm ou não espaços
        'Seu nome tem {n} letras'
        'A primeira letra do seu nome é {primeira_letra}'
        'A última letra do seu nome é {ultima_letra}'
    Se nada for digitado:
        'Desculpe, você deixou campos vazios'
        
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome != "" and idade != "":
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(" " in nome)
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[len(nome) - 1 ]}')
else:
    print('Desculpe, você deixou campos vazios')

#EXERCÍCIO 2#

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = int(input("Digite um número inteiro: "))

if (numero % 2) == 0:
    print('Numero {} é par'.format(numero))
elif (numero % 3) == 0:
    print(f'Número {numero:,.2f} é impar')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = int(input("Informe a hora: "))

if hora >= 0 and hora <= 11:
    print('Bom dia!!!!')
elif hora >= 12 and hora <= 17:
    print('Boa tarde!!!!')
else:
    print('Boa noite!!!!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_numero = input('Informe seu primeiro nome: ')
tamanho_nome = len(primeiro_numero)

if tamanho_nome <= 4:
    print('Seu nome é curto')
elif tamanho_nome in (5,6):
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')

#EXERCÍCIO 3#

nome = 'Victor Hugo'
qtd_caracteres = len(nome)
x = 0
texto = ''

while x <= qtd_caracteres:

    try:
        texto_inicio = '*' + nome[x]
        texto = texto + texto_inicio
    except:
        print(texto)
        break
    
    x += 1  

#EXERCÍCIO 4 - CALCULADORA#

while True:
    print('Informe a operação desejada!')
    operacao = int(input('1 - SOMA  2 - SUBTRAÇÃO 3 - MULTIPLICAÇÃO 4 - POTENCIAÇÃO 5 - DIVISÃO 6 - SAIR: '))

    if operacao == 1:

        while True:

            try:
                primeiro_numero = int(input('Informe o 1º número: '))
                break
            except:
                print('Informe um número válido!')
                continue
        
        while True:

            try:
                segundo_numero = int(input('Informe o 2º número: '))
                break
            except:
                print('Informe um número válido!')
                continue

        resultado = primeiro_numero + segundo_numero
        
        print(f'O resultado é {resultado}')

    elif operacao == 2:

        while True:

            try:
                primeiro_numero = int(input('Informe o 1º número: '))
                break
            except:
                print('Informe um número válido!')
                continue
        
        while True:

            try:
                segundo_numero = int(input('Informe o 2º número: '))
                break
            except:
                print('Informe um número válido!')
                continue

        resultado = primeiro_numero - segundo_numero

        print(f'O resultado é {resultado}')

    elif operacao == 3:

        while True:

            try:
                primeiro_numero = int(input('Informe o 1º número: '))
                break
            except:
                print('Informe um número válido!')
                continue
        
        while True:

            try:
                segundo_numero = int(input('Informe o 2º número: '))
                break
            except:
                print('Informe um número válido!')
                continue

        resultado = primeiro_numero * segundo_numero

        print(f'O resultado é {resultado}')

    elif operacao == 4:

        while True:

            try:
                primeiro_numero = int(input('Informe o 1º número: '))
                break
            except:
                print('Informe um número válido!')
                continue
        
        while True:

            try:
                segundo_numero = int(input('Informe o 2º número: '))
                break
            except:
                print('Informe um número válido!')
                continue

        resultado = primeiro_numero ** segundo_numero

        print(f'O resultado é {resultado}')

    elif operacao == 5:

        while True:

            try:
                primeiro_numero = int(input('Informe o 1º número: '))
                break
            except:
                print('Informe um número válido!')
                continue
        
        while True:

            try:
                segundo_numero = int(input('Informe o 2º número: '))
                break
            except:
                print('Informe um número válido!')
                continue

        resultado = primeiro_numero / segundo_numero

        print(f'O resultado é {resultado}')
    else:

        break

