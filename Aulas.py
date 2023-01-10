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

#F-STRINGS#
nome = "Victor"
altura = 1.86
valor = 1000000

texto = f'{nome} é o melhor, pode não ser, mas na cabeça do {nome}, ele é. Além do mais ele tem {altura:.1f}M de altura.'
print(texto)
#Colocar o f antes das aspas nas strings permite inserir as variáveis no meio da frase.

#No nome da variável delimitado por chaves, é possível escolher o número de casas decimais colocando :.2f trocando o 2 pelo número de casas desejado.

texto2 = f'{nome} tem {valor:,.2f} na sua conta bancária'
print(texto2)
#Em caso de valores como dinheiro é possível realizar a pontuação correta colocando :,.2f após a variável.

#.FORMAT#
nome = "Maria"
curso = "Odontologia"

print('a {} cursa {}'.format(nome, curso))
#As variáveis são postas de acordo na ordem expressa dentro do .format ah não ser que coloquemos indices dentro das chaves.

#Dentro da chave pode ser posto o parâmetro para número decimais e etc..

#É possível colocar nomes como parâmetros dentro do .format, quando um argumento é nomeado com parâmetro todos os próximos argumentos também vão
#precisar, e os argumentos nomeados precisam ser chamados pelo parãmetro dentro da chave ao invés do indice.

#INPUT#
nome = input('Qual o seu nome? ')

print(f'O seu nome é {nome}')

#Podemos usar o input para coletar dados do usuário.

#IF/ELIF/ELSE#
entrada = input('Você quer entrar ou sair? ')

if entrada == "entrar":
    print("Você entrou")
elif entrada == "sair":
    print("Você saiu")
else:
    print("Você não digitou nenhuma das opções")




