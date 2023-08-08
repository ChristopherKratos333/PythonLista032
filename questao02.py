'''
Desenvolver um programa que faça duas perguntas: o valor referente às horas atuais e o valor referente aos
minutos atuais. Exemplo, se agora são 09:35h o usuário deverá informar como resposta às horas atuais o valor
09 e como resposta aos minutos atuais o valor 35. Em seguida o programa deverá apresentar como resposta
quantos minutos já se passaram desde às 00:00h deste dia.
'''

hora = int(input(f"Digite as horas atuais, se for por ex 09:05 digite agora '09' e depois '05': "))
minuto = int(input(f"Digite agora os minutos: "))

minutos = 60 * hora + minuto

print(f"Desde às 00:00 se passaram {minutos} minutos.")