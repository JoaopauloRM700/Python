#1. Qual o valor médio de PIB per capita da 
# cidade de Manaus no período que abrange o dataset? 
import os 
#import '/DesafioPython-Trainee/main'
#import 'D:/workspace/python/DesafioPython-Trainee/main' 
# # Tentei realizar o import para acessar os processos que fiz no outro documento mas sem sucesso

os.system('cls')

lista= []
   # Leitura do Arquivo, utilizando o encoding para processar os caracteres especiais 
with open('D:/workspace/python/DesafioPython-Trainee/dataset/pib_municipio_2010_a_2018.txt','rt',encoding='utf-8') as dataset: 
   for l  in dataset:
      data = dataset.readline()
      data = data.split(';')
      lista.append(data)
     
x = 0
tamanho = len(lista) 
qt = 0
pib = 0 


while x < tamanho:
   #print(lista[x])
   if lista[x][3] == "Manaus":
      print(lista[x][0]+":"+lista[x][13])
      pib += float(lista[x][13])
      qt+=1
   x+=1
mediaPib = pib / qt
""" 
print(pib)
print(qt)
print(mediaPib) 
# Prova Real dos Calculos da Primeira Questão
"""

with open('D:/workspace/python/DesafioPython-Trainee/questao_01/saida_q1.txt','wt',encoding='utf-8') as q1: 
   dataset.write(str(mediaPib)+" foi o valor médio de PIB per capita da cidade de Manaus no período que abrange a base de dados")

dataset.close()
q1.close()





#matriz = [lista]
#print(matriz[1][0])
