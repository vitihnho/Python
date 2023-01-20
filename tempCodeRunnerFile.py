
frase_secreta = 'RIBEIRAO'
print(frase_secreta.find('A',0))

#teste = frase_secreta[0:5] + 'x' + frase_secreta[6:]
#print(teste)

for frase_oculta in frase_secreta:
    frase_oculta = '*' * len(frase_secreta)

x = 0
"""frase_oculta = frase_oculta[0:0] + letra + frase_oculta[1:]
frase_oculta = frase_oculta[0:5] + letra + frase_oculta[6:]
print(frase_oculta)
while x < len(frase_secreta):
                
    indice = frase_secreta.find(letra, x)
    print(indice)
    frase_oculta = frase_oculta[0:(indice - 1)] + letra + frase_oculta[indice:]
    x += 1"""


print(frase_oculta)

while frase_oculta != frase_secreta:

    try:
        letra = str(input('Informe uma letra: ')).upper()

        if len(letra) > 1:
            print('Apenas UMA letra')
            continue

    except:
        print('Informe apenas letras')
        continue

    x = 0
    while True:

        if letra in frase_secreta:

            while x < len(frase_secreta):
                
                indice = frase_secreta.find(letra, x)

                if indice == -1:
                    print('Tente novamente')
                    break
                else:
                    frase_oculta = frase_oculta[0:(indice)] + letra + frase_oculta[indice+1:]
                x += 1
        else:
            print('Tente novamente')

        print(frase_oculta)

        break