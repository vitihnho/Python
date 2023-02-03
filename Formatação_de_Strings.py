#FORMATAÇÃO COM STRINGS

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

#FORMATAÇÃO COM F-STRINGS#

    #Ajusta caracteres e completa com espaços vazios se necessário ou alguns caracteres caso sejam informados.

nome = 'Victor'
print(f'{nome: >12}') #DIREITA
print(f'{nome: <12}') #ESQUERDA
print(f'{nome: ^12}') #MEIO
print(f'{nome:$<12}') #ESQUERDA

    #Formatação de números, colocando vírcula e escolhendo as casas decimais.
    
valor = 1000.50
print(f'{valor=:,.1f}') #Quando atribuímos igual na frente da variável, o nome dela vem junto ao valor.

    #Fatiamento de strings | Função len

var = "Ooh My God"

print(var[-5]) #Pega o elemento de trás para frente na variável.

print(var[4:6]) #Delimita a seleção ou em caso de apenas um valor informado antes dos ':', todo o restante é retornado. 
                #O python entende as posições de vetor de modo diferente, então sempre o último elemento precisa ser o que você
#busca + um, se não ele é ignorado.

print(len(var)) #Conta o número de caracteres.

print(var[0:len(var):2]) #Devolve os caracteres de 0 até o último (Já que estou passando como paramêtro o tamanho do vetor completo) 
                         #E pula de 2 em 2.

#.FORMAT#
nome = "Maria"
curso = "Odontologia"

print('a {} cursa {}'.format(nome, curso))
#As variáveis são postas de acordo na ordem expressa dentro do .format ah não ser que coloquemos indices dentro das chaves.

#Dentro da chave pode ser posto o parâmetro para número decimais e etc..

#É possível colocar nomes como parâmetros dentro do .format, quando um argumento é nomeado com parâmetro todos os próximos argumentos também vão
#precisar, e os argumentos nomeados precisam ser chamados pelo parãmetro dentro da chave ao invés do indice.

#INPUT#

nome = input('Qual o seu nome? ') #Podemos usar o input para coletar dados do usuário.

print(f'O seu nome é {nome}')

#INTERPOLAÇÃO#

nome = 'Victor'
preco = 1000.25
var = '%s, o valor é de R$ %f' % (nome,preco)
print(var)

#DESCOBRIR O HEXADECIMAL DE UM NÚMERO

var = 20
teste = 'O hexadecimal de %d é %08X' % (var,var)
print(teste)

#Trocar a saída da string

string = input('Digite seu nome: ')
nova_string = str.lower(string) #Transforma todo conteúdo do texto em letras minusculas.
print(nova_string)

teste = nova_string.startswith('v') #Devolve verdadeiro ou falso se a string começa ou não com a letra indicada.
print(teste)

#Replace

cpf = '537.559.843-84' \
    .replace('.',"") \
    .replace('-',"")

print(cpf)

