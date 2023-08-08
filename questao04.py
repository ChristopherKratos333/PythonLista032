'''
Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura2
 - Obs: peso em quilos e altura em metros.
'''

peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura * altura)

print(f"O seu IMC é: {imc:.2f}")