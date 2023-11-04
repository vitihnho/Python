
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

s3 = s1 ^ s2
print(s3)