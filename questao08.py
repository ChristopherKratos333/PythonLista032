'''
Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
'''

custo = float(input("Digite o custo do seu produto: "))
acrescimo = float(input("Digite um percentual de acréscimo para o seu produto: "))

valor_venda = custo + custo * acrescimo / 100

print(f"O valor de venda do seu produto é: {valor_venda}")
