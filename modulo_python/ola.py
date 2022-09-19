"""
peso = float(73.5)
endereco : str
endereco = "Ola mundo 2"

print(" ola mundo" + endereco)

lista = ["A","B", 1 ,1.2, False, True]

print ("Valor:"+str(lista[5]))
print("Tipo: "+str(type(lista[5])))


dicio = { # Dictionary
    "nome":"joao paulo",
    "idade": 23,
    "nacionalidade":"Brasileiro"
}

tv = { # Dictionary
    "Marca":"Sansung",
    "Modelo": "Smart",
    "Polegadas":"50'",
    "Resolucao":"4k",
    "preco": 3999.99
}

print(dicio["idade"])
print(tv.get("preco")) 
"""

import os


nota1= int(input())
peso1 = int(input())
nota2= int(input())
peso2 = int(input())
nota3 = int(input())
peso3 = int(input())


Media = (nota1+nota2+nota3)/3

if nota1 >=0:
    executa:True
if nota2 >=0:
    executa:True
if nota3 >=0:
    executa:True

if executa == True:
    Media = (nota1+nota2+nota3)/3



    