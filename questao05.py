'''
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número.
'''

a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))

soma = a + b
subtracao = a - b
subtracao2 = b - a
multiplicacao = a * b
div = a / b
restodadiv = a % b

print(f"A soma entre eles: {soma}")
print(f"A subtração do primeiro pelo segundo: {subtracao}")
print(f"A subtração do segundo pelo primeiro: {subtracao2}")
print(f"A multiplicação entre eles: {multiplicacao}")
print(f"A divisão do primeiro pelo segundo: {div}")
print(f"O resto da divisão do primeiro pelo segundo: {restodadiv}")

