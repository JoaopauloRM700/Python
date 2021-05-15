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
vladcbruto = 0 
vladcbrutoTotal = 0
MedBruto18 = []

while x < tamanho:
    #print(lista[x])
    if lista[x][1] == "AM" and lista[x][0]=="2018":  # Extraio a media dos serviços 
        #print(lista[x][0]+":"+lista[x][13])
        MedBruto18.append(float(lista[x][8]))
        vladcbruto += float(lista[x][8])
        qt+=1
    x+=1
#BMedServc = vladcbruto / qt
BMedserv18 = sum(MedBruto18)/len(MedBruto18)

#print(BMed18)

MedBrutoTotal=[]
x = 0
tamanho = len(lista) 
qt = 0
vladcbruto = 0 
vladcbrutoTotal = 0

while x < tamanho:
    #print(lista[x])
    if lista[x][1] == "AM" and lista[x][0]=="2018": # Extraio a media do valor adicionado total 
        #print(lista[x][0]+":"+lista[x][13])
        MedBrutoTotal.append(float(lista[x][10]))
        vladcbrutoTotal += float(lista[x][10])
        qt+=1
    x+=1

#BMedtotal1 = vladcbrutoTotal / qt
BMedtotal2= sum(MedBrutoTotal)/len(MedBrutoTotal)
#print(BMedtotal2)

prop = BMedserv18/BMedtotal2 # Calculo de porporcão

#print("A proporção foi de "+str(prop)+" ou "+str(prop*100)+"% em Porcentagem")

with open('D:/workspace/python/DesafioPython-Trainee/questao_03/saida_q3.txt','wt',encoding='utf-8') as q3: 
   q3.write("A proporção foi aproximadamente de "+str(round(prop,5))+" ou "+str(round(prop*100 , 2))+"% em Porcentagem")
#round para ficar visivelmente mais agradavel
dataset.close()
q3.close()
