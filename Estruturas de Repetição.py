#Estruturas de Repetição

#WHILE
#Executa uma ação enquanto uma condição for verdadeira

condicao = True

while condicao:
    print("Sou o melhor") #Nunca para, já que a condição sempre vai ser verdadeira

    break #Só sai do looping com o break. Pode ser posto em uma condição, se a condição for verdadeira então break.

#CONTINUE
#Pode ser utilizado para pular parte da execução do código.

x = 0

while x < 10:
    x += 1

    if x == 5:
        continue #Dessa forma o número 5 não aparece na execução!

    print(x)

#FOR#

nome = 'Victor'

for letra in nome:
    print(letra)

#RANGE range(start, stop, step)

for numero in range(1, 10, 2):
    print(numero)
