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

frase = ['maria','é','linda']
print(*frase)
#Ao usar o asterístico, selecionamos todas os campos dentro do vetor.++--

#Operação Ternária

print('Valor' if True else 'nValor')

#DICIONÁRIO (Dict)

pessoa = {

    'nome': 'Victor',
    'sobrenome': 'Ferreira',
    'idade': 18,
    'altura': 1.8,

}

print(pessoa, type(pessoa))
print(pessoa['nome'])

#Podemos editar, apagar e inserir novos dados dentro do dicionário.

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Victor Hugo'

print(pessoa)

pessoa['sobrenome'] = 'Ferreira'

print(pessoa)

del pessoa['sobrenome']

print(pessoa)

#Podemos verificar a existência de um valor dentro do dicionário.

if pessoa.get('nome') is None:
    print('VAZIO')
else:
    print(f'O nome é {pessoa["nome"]}')

#MÉTODOS#

#len

pessoa = {

    'nome': 'Victor',
    'sobrenome': 'Ferreira'
}

print(len(pessoa)) #Retorna a quantidade de chaves dentro do dicionário
print(list(pessoa.keys())) #Retorna as chaves
print(list(pessoa.values())) #Retorna os valores da chave

pessoa.setdefault('idade', '18') #Definimos um padrão para a chave, mesmo que ela não exista.
print(pessoa['idade']) #Dessa forma a chave é criada também.

print(pessoa)

#COPY

d1 = {

    'a': '10',
    'b': '20'
}

d2 = d1.copy() #Dessa forma copiamos outro dicionário.

d2['a'] = '23' #Se não tivessimos recebido a cópia, isso mudaria a chave dentro dos dois dicionários.
#Mas esse método é apenas uma cópia rasa, se tivermos uma lista dentro do dicionário copiado, ele não é copiado, só aponta
#para o mesmo lugar
print(d1)
print(d2)

import copy

#Para resolver o problema podmos usar um deepcopy, copiando todas as chaves.

d3 = copy.deepcopy(d1)
print(d3)

#GET

p1 = {
    'nome': 'Victor',
    'sobrenome': 'Ferreira',
}

print(p1.get('nome'))
#Retorna o conteúdo, caso não exista por padrão retorna none, mas podemos especificar o que vai ser retornado

print(p1.get('idade','Inexistente'))

#No dicionário podemos utilizar o pop para armazenar um conteúdo e excluí-lo do dicionário.

nome = p1.pop('nome')
print(p1)

#popitem remove a última chave, por conta disso não pode ser passado parâmetro.

nome = p1.popitem()
print(nome)

# update atualiza o dicionário

# podemos escrever assim,
p1.update({

    'nome' : 'José'

})

# ou assim
p1.update(nome = 'Augusto')

#Também funciona por tuplas

tupla = ('nome','Renato'),

p1.update(tupla) #O MESMO FUNCIONA PARA LISTAS
print(p1)

#SET
#Muito útil para remover valores duplicados de uma lista.
#Não promote entregar na ordem o conteúdo

s1 = set('Abc')
print(s1)

lista = [1,2,33,3,3,3]
st = set(lista)
print(st)

s2 = set()
s2.add('Victor') #Dessa forma podemos incluir elementos dentro do nosso set
print(s2)
s2.add(123)
s2.discard('Victor')
print(s2)

# O set pode ser utilizado como os conjuntos da matemática.

lista1 = [1,2,3,4,5,6]
s1 = set(lista1)

lista2 = [4,5,6,89]
s2 = set(lista2)

s3 = s1 | s2 # Está em um ou eu outro
print(s3)

s3 = s1 & s2 # Está nos dois
print(s3)

s3 = s1 - s2 # Diferença do 1º com o 2º
print(s3)

s3 = s1 ^ s2 #Retorna a difença literal, todos os elementos do 2º que não está no 1°
print(s3)

