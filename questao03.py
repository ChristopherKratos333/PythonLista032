'''
Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
'''

kg = float(input("Digite seu peso em Kg: "))
metro = float(input("Digite sua altura em metros: "))

g = kg * 1000
cm = metro * 100

print(f"O seu peso em gramas é {g} e sua altura em centímetros é {cm}")