'''
Exercício: crie um programa que 
calcule a média aritmética das notas de um aluno.
O programa deve pedir para o usuário digitar
 as notas 1, 2 e 3.
O programa deve guardar as respostas em uma lista
Em seguida deve somar as notas e dividi-las 
 por 3 colocando=as na tela.

'''

print ("Média de notas")

lista =[]


n = float(input("Digite sua primeira nota"))
n = float(input("Digite sua segunda nota"))
n = float(input("Digite sua terceira nota "))

lista.append(n)
lista.append(n)
lista.append(n)

soma = lista[0] + lista[1] + lista[2]
media = soma / 3

print("Esta é a média das suas notas: ", media)