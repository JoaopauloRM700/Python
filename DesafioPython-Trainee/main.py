import os
os.system('cls')

"""
LER, CRIAR E MODIFICAR ARQUIVOS

'r' -> Usando somente para ler algo
'w' -> Usado somente para escrever algo
'r+' -> Usado para ler e escrever algo
'a' -> Usado para acrescentar algo



"""

# Leitura do Arquivo, utilizando o encoding para processar os caracteres especiais 
with open('D:/workspace/python/DesafioPython-Trainee/dataset/pib_municipio_2010_a_2018.txt','r',encoding='utf-8') as dataset: 
   data = dataset.read()

""" # Replace ; por ,
data = data.replace(';', ',')

#Reescrevo no documento
with open('D:/workspace/python/DesafioPython-Trainee/dataset/pib_municipio_2010_a_2018.txt','w',encoding='utf-8') as dataset: 
   dataset.write(data)
 """

#Substituir ; por , 
""" with open('D:/workspace/python/DesafioPython-Trainee/dataset/pib_municipio_2010_a_2018.txt','r+',encoding='utf-8') as dataset: 
    for x in dataset:
        dataset.write (x.replace(";",","))
         """

dataset.close()
