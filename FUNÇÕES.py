#FUNÇÕES

#Definindo funções

def printer(a, b, c):
    print(a, b, c)

printer(1, 2, 4)

#Utilizamos funções para realizar determinadas ações apenas mudando parâmetros.

def soma(x, y, z = 1):

    if z is not None:
        print(f'Z não é nulo, mas X = {x} e Y = {y}')
    else:
        print('Z é nulo')

soma(1,2)

#ARGS

def soma(*args): #Dessa forma podemos não especificar em quantidade os argumentos das funções.
    #O args serve como empacotador
    total = 0

    for numero in args:
        total += numero
    
    return total

soma_acumulada = soma(1,2,3,4,5)
print(soma_acumulada)

#Ao invés de criar essa função soma, poderíamos usar o sum, uma função pronta do próprio python.

print(sum((1,23,4,353,6))) #O sum recebe apenas 1 argumento, então devemos delimitar o conteúdo como em uma tupla.

#HIGHER ORDER FUNCTION
    #Funções que recebem outras funções e podem retorná-las



