import os
os.system('cls')

"""
LER, CRIAR E MODIFICAR ARQUIVOS

'r' -> Usando somente para ler algo
'w' -> Usado somente para escrever algo
'r+' -> Usado para ler e escrever algo
'a' -> Usado para acrescentar algo

"""


lista= []
   # Leitura do Arquivo, utilizando o encoding para processar os caracteres especiais 
with open('D:/workspace/python/DesafioPython-Trainee/dataset/pib_municipio_2010_a_2018.txt','rt',encoding='utf-8') as dataset: 
   for l  in dataset:
      data = dataset.readline()
      data = data.split(';')
      lista.append(data)
     
x = 0
tamanho = len(lista) 
qt = 1
pib = 0 

while x < tamanho:
   if lista[x][0] == "2010" and lista[x][3]=="Manaus":
      print(lista[x])

   x+=1 

#Reescrevo no documento
""" with open('D:/workspace/python/DesafioPython-Trainee/dataset/pib_modificado','wt',encoding='utf-8') as dataset: 
      dataset.write(str(lista))
#Prova Real das Modificações
 """

#print(lista[1][3])



dataset.close()
