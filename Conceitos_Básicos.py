# -*- coding: windows-1252 -*-

nome = "jose"
sobrenome = "almeida"
idade = int(19)
ano_de_nascimento = "05/02/2003"
if int(idade) >= 18:
    maior_de_idade = "Sim"
else:
    maior_de_idade = "Não"
altura = 1.86

print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", idade)
print("Ano de nascimento:", ano_de_nascimento)
print("Maior de idade?", maior_de_idade)
print("Altura: ", altura)
 
#Calculando IMC

nome = "Victor"
peso = 76
altura = 1.86
imc = peso / (altura ** 2)

print(nome, "tem", altura, "de altura, pesa", 76, "quilos e seu IMC é",round(imc))

#Uso do Try e Excessions

numero = input('Digite um número: ')

print(numero.isdigit()) 
"""
Verifica se o número é ou não um digito
O problema desse input, é que ele só considera número os números inteiros.
"""

try:
    numero_float = float(numero)
    print("Float: ",numero_float)
    print(f'O dobro do número {numero_float} é {numero_float * 2}')
except:
    print('Isso não é um número')

"""
Conceitos Básicos de boas práticas

CONSTANTE -> "Variável" que nunca muda, expressada por letras maiusculas

Muitas condições em um mesmo IF (ruim)
Muitas linhas endentados uma dentro da outra (ruim)
Utilizar barra invertido no código \
    Para dizer ao python que o código tem continuação

"""

#Variáveis são imutáveis

string_teste = "Victor Hugo"
#string_teste[3] = "abc" Na teoria eu estou tentando substituir a 3º posição do meu vetor por "abc"

string_teste2 = f'{string_teste[:3]}abc{string_teste[3:]}'
print(string_teste2)