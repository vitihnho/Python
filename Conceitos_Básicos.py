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