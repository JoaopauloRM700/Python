#3. Qual a proporção do valor adicionado bruto médio 
# do setor de serviços em relação ao valor adicionado 
# bruto total médio no estado do Amazonas no ano de 2018? 

import os
os.system('cls')
lista= []
MedPibEstados = []
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
MedBruto18 = []
while x < tamanho:
    #print(lista[x])
    if lista[x][1] == "AM" and lista[x][0]=="2018":
        #print(lista[x][0]+":"+lista[x][13])
        MedBruto18.append(float(lista[x][8]))
        pib += float(lista[x][8])
        qt+=1
    x+=1
BMed2018 = pib / qt
BMed18 = sum(MedBruto18)/len(MedBruto18)

print(str(BMed2018)+" : "+str(BMed18))

   



dataset.close()
