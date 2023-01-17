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