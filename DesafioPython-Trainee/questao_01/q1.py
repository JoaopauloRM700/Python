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
#qt = 0
#pib = 0 
pibs = []
"""

Algumas partes comentadas são porque eu havia feito de uma forma mas descobri que havia outra forma melhor para realizar o mesmo
processo, deixando mais dinamico. Deixe eles no codigo para fazer comparação e validação

"""
while x < tamanho:
   #print(lista[x])
   if lista[x][3] == "Manaus":
      #print(lista[x][0]+":"+lista[x][13])
      pibs.append(float(lista[x][13])) # adiciona os pibs anuais a lista de pibs
      #pib += float(lista[x][13])
      #qt+=1
   x+=1
#mediaPib = pib / qt
mediaMA = sum(pibs) / len(pibs) # tira a media somando os pibs e dividindo pela quantidade armazenada
#print(pib)
#print(qt)
print(round(mediaMA,4)) #Arredondamento aplicado para mostrar so 4 casas decimais
#print(mediaPib) 
# Prova Real dos Calculos da Primeira Questão


with open('D:/workspace/python/DesafioPython-Trainee/questao_01/saida_q1.txt','wt',encoding='utf-8') as q1: 
   q1.write(str(round(mediaMA,4))+" foi o valor médio de PIB per capita da cidade de Manaus no período que abrange a base de dados")
#Escrita da resposta no arquivo de saida e fechamento dos arquivos
dataset.close()
q1.close()





#matriz = [lista]
#print(matriz[1][0])
