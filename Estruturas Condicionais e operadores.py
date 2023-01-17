#Estruturas Condicionais e operadores lógicos#

#IF/ELIF/ELSE#
entrada = input('Você quer entrar ou sair? ')

if entrada == "entrar":
    print("Você entrou")
elif entrada == "sair":
    print("Você saiu")
else:
    print("Você não digitou nenhuma das opções")

#CONDIÇÃO COM OPERADORES
numero1 = int(input("Primeiro número: "))
numero2 = int(input("Segundo número: "))

if numero1 >= numero2:
    print(f"{numero1} é maior ou igual a {numero2}")
else:
    print(f"{numero2} é maior do que o {numero1}")

#OPERADOR LÓGICO AND e OR
opcao = input("SIM OU NÃO: ")
senha_dig = int(input("Digite sua senha: "))

if (opcao == "SIM" or opcao == "sim") and senha_dig == 123:
    print("Parabéns, vc entrou")
else:
    print("Tenta dnv")

a = input("Senha: ") or "Sem senha"
print(a)

#Da forma apresentada à cima, é possível devolver um valor caso nada seja digitado.

#OPERADOR LÓGICO NOT
senha = input("Digite sua senha: ")

if senha != '123':
    print("Errou a senha!")

#OPERADOR LÓGICO IN
nome = 'Victor'

print('V' in nome)
print('V' not in nome)

variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a)


