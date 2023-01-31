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

#LIST#

#Para criar uma lista é necessário atribuir chaves.

lista = []
print(type(lista))

lista = ['Victor',18,'Analista'] #Podemos atribuir n variáveis dentro de uma lista e com tipos diferentes.
print(lista[2]) #Retornar o valor separadamente trazendo o indice como parâmetro.

lista[2] = 'O melhor' #Alterar o valor através do parâmetro.
print(lista[2])

del lista[2] #Podemos apagar o conteúdo da lista com del
print(lista)

lista.append(35) #Adiciona elemento no final da lista
print(lista)

lista.pop() #Remove o último elemento da lista
del lista[-1] #Remove o último elemento da lista
print(lista)

lista.clear() #Remove todos os elementos da lista
print(lista)

lista.insert(0,"Calica") #Adiciona o elemento na posição informada, se já existir algo o elemento existente é posto à frente
print(lista)

#CONCATENANDO LISTAS#

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b #Concatenamos as duas listas
print(lista_c)

lista_a.extend(lista_b) #Extendemos os valores da lista_a com os valores da lista_b
print(lista_a) #OBS: Se dermos um print na linha de cima o valor retornado será 'none', já que aquilo apenas atribui um valor e não retorna.

#DESEMPACOTAR

lista = ['Victor','Hugo','Ferreira']
nome1, nome2, nome3 = lista
print(nome2)

#No caso à cima especificamos o número exato de elementos da lista para que não tenha nenhum erro.
#Mas se só quero pegar o 1º elemento e os demais posso ignorar, consigo fazer isso.

nome1, *resto = lista
print(nome1, resto)

#Geralmente quando queremos mostrar que o resto não será utilizado, usamos _

nome1, *_ = lista
print(nome1, _)

#Tupla é uma lista imutável, ou seja, não conseguimos trocar seus valores.

tup = 'victor','hugo','ferreira'
tup[2] = 'oto' #Apresenta o erro por causa da sua especificação, tuplas não mudam.

#ENUMERATE

lista = ['Victor','Hugo','Ferreira']

lista_enumerada = list(enumerate(lista)) #O enumerate númera os elementos e pode receber como parâmetro o ponto de início
print(lista_enumerada)

lista_enumerada = list(enumerate(lista, start=59))
print(lista_enumerada)

#SPLIT STRIP

frase = 'O cachorro, ele é louco'
frase_sep = frase.split(',')
print(frase_sep)

for i, frase in enumerate(frase_sep):
    print(frase.strip())

#JOIN
#une strings

frase = 'abc'
frase_unida = '*'.join(frase)
print(frase_unida)