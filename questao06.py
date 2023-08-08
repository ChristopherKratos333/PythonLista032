'''
Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês.
'''


nome = input("Informe o nome do vendedor: ")
salario = float(input("Digite o seu salário fixo: "))
vendas = float(input("Digite o total de vendas dele(a) no mês em dinheiro: "))

comissao = vendas * 0.15
completo = salario + comissao

print(f"Olá {nome}, seu salário fixo é {salario}, sua comissão é {comissao} e seu salário completo é {completo}")