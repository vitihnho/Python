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

#EXERCÍCIO 5#

frase = 'Sou o melhor, posso não ser' \
    'mas na minha cabeça, sou o melhor'.lower()

x = 0

letra_que_mais_apareceu = " "
qtd_de_vezes = 0

while x < len(frase):
    letra_atual = frase[x]

    if letra_atual == " ":
        x +=1
        continue
    else:
        qtd = frase.count(letra_atual)

        if qtd_de_vezes < qtd:
            qtd_de_vezes = qtd
            letra_que_mais_apareceu = letra_atual

        x +=1

print(f'A letra que apareceu mais vezes é "{letra_que_mais_apareceu}" totalizando {qtd_de_vezes} aparições')
print(x)

#EXERCÍCIO 6#

import os

frase_secreta = 'RIBEIRAO'

for frase_oculta in frase_secreta:
    frase_oculta = '*' * len(frase_secreta)

print(frase_oculta)

qtd_tentativas = 0

while frase_oculta != frase_secreta:

    while True:

        letra = str(input('Informe uma letra: ')).upper()

        qtd_tentativas += 1

        if letra in ('0','1','2','3','4','5','6','7','8','9'):
            print('Informe apenas letras.')
            continue
        elif len(letra) > 1:
            print('Apenas UMA letra')
            continue
        elif letra == "":
            print("Digite algo!")
            continue
        else:
            break
        
    x = 0

    while True:

        if letra in frase_secreta:

            while x < len(frase_secreta):
                
                indice = frase_secreta.find(letra, x)

                if indice == -1:
                    break
                else:
                    frase_oculta = frase_oculta[0:(indice)] + letra + frase_oculta[indice+1:]
  
                x += 1
        else:
            print('Tente novamente')

        print(frase_oculta)

        break

os.system('cls') #LIMPA O TERMINAL
print('VOCÊ GANHOU')
print(f'A frase oculta é "{frase_oculta}"')
print(f'A quantidade de tentativas foi de {qtd_tentativas}')

#EXERCÍCIO 7#

lista = ["Victor","Maria","Birigo"]

for indice, produto in lista:
    print(indice, produto)
for indice in [0, 1, 2]:
    print(indice)

#EXERCÍCIO 8#

import os
lista = []

while True:
    
    opcao = input('Selecione uma das opções\n[i]nserir, [a]pagar, [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Informe o valor: ')
            
        if valor == "":
            print('Informe um valor')
            continue
        else:
            lista.append(valor)

    elif opcao == 'a':

        os.system('cls')

        indice = int(input('Informe o indice à ser retirado: '))

        if len(lista) < indice:
            print('Indice Inválido')
        else:
            try:
                lista.pop(indice)
            except:
                print('Lista Vazia')

    elif opcao == 'l':
        os.system('cls')
        lista_numerada = list(enumerate(lista))

        for indice, produto in enumerate(lista):
            print(indice, produto)
            
    break

#EXERCÍCIO 9#

digitos = input('Informe os 9 primeiros dígitos do seu CPF: ')

if len(digitos) > 9:
    print(f'Informe apenas 9 digitos você digitou {len(digitos)} digitos.')
else:
    num1, num2, num3, num4, num5, num6, num7, num8, num9 = digitos
    total = (int(num1) * 10) +( int(num2) * 9) + (int(num3) * 8) + (int(num4) * 7) +( int(num5) * 6) +( int(num6) * 5 )+ (int(num7) * 4 )+ (int(num8) * 3) +( int(num9) * 2)
    
    primeiro_digito = (total * 10) % 11

    if primeiro_digito > 9:
        primeiro_digito = 0

    print(primeiro_digito)

    total2 = (int(num1) * 11) +( int(num2) * 10) + (int(num3) * 9) + (int(num4) * 8) +( int(num5) * 7) +( int(num6) * 6 )+ (int(num7) * 5 )+ (int(num8) * 4) +( int(num9) * 3) + (int(primeiro_digito) * 2)

    segundo_digito = (total2 * 10) % 11

    print(segundo_digito)

#EXERCÍCIO 10#

def mult(*num):
    total = 1

    for numero in num:
        total *= numero

    return total

multiplica = mult(1,3,5)
print(multiplica)

def tipo(multiplica):

    if multiplica % 2 == 0:
        print(f'Número {multiplica} é par!')
    else:
        print(f'Número {multiplica} é ímpar!')

tipo(multiplica)
    
#EXERCÍCIO 11#

def duplicar(numero):
    return numero * 2

n2 = duplicar(3)
print(n2)

def multiplicador(multp):
    def multiplicar(numero):
        return numero * multp
    return multiplicar

n2 = multiplicador(3)
print(n2(3))

#EXERCÍCIO 12#

perguntas = [

    {
        'Pergunta': 'Quem parece um coala, mas nem do plata terra é?',
        'Opções': ['Stitch','Pikachu','Pairulito'],
        'Resposta': 'Stitch',
    },

    {
        'Pergunta': 'Onde somos todos atletas?',
        'Opções': ['Em casa','Na Academia','Na Growth'],
        'Resposta': 'Na Growth',
    },

    {
        'Pergunta': 'Sou proibido igual poze do rodo na...',
        'Opções': ['Igreja','Televisão','Cadeia'],
        'Resposta': 'Televisão'
    },

]

qtd_acertos = 0
acertou = False
for perguntas in perguntas:
    print('Pergunta:', perguntas['Pergunta'])
    print()

    opcoes = perguntas['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()

    escolha = input('Escolha uma das opções: ')

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < len(opcoes):
            if opcoes[escolha_int] == perguntas['Resposta']:
                acertou = True
                
        if acertou:
            qtd_acertos += 1
            print('Você Acertou 👍')
        else:
            print("Você Errou 😢")

print(f'Você obteve {qtd_acertos} acertos de {len(perguntas)} perguntas')