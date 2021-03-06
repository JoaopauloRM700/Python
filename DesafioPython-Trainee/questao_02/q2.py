#2. Qual o ranking de estados por média de PIB per capita no ano de 2010?
import os
os.system('cls')
lista= []
MedPibEstados = [] # Esse list virara uma Matriz para classificação do estados
   # Leitura e tratamento do Arquivo, utilizando o encoding para processar os caracteres especiais e o split para trasformar o texto em matriz 
with open('D:/workspace/python/DesafioPython-Trainee/dataset/pib_municipio_2010_a_2018.txt','rt',encoding='utf-8') as dataset: 
   for l  in dataset:
      data = dataset.readline()
      data = data.split(';')
      lista.append(data)
     
x = 0
tamanho = len(lista) 
qt = 0
pib = 0 
pibs = []

def MediaEstado(estado):
   x=0
   qt = 0
   pib = 0 
   while x < tamanho:
      if lista[x][0]=="2010" and lista[x][1] == estado:  #Loop com condicional para extrair os dados necesarios 
         #print(lista[x][0]+":"+lista[x][13])
         pib += float(lista[x][13])
         pibs.append(float(lista[x][13]))
         qt+=1
      x+=1
   mediaPib = pib / qt
   #mediaEst = sum(pibs)/len(pibs)
   listaPib = [mediaPib,"ESTADO:"+estado+" | PIB:"+str(mediaPib)] # retorno uma lista com duas informações, a media em float e a String com Estado + PIB
   return listaPib 
   

estados =["RO","AC","AM","RR","PA","AP","TO","MA","PI","CE","RN","PB","PE","AL","SE","BA","MG","ES","RJ","SP","SC","RS","MT","GO","DF"]
tamEst = len(estados)
est = 0
while est < tamEst:
   MedPibEstados.append(MediaEstado(estados[est]))
   est+=1



print(len(estados))
rank = sorted(MedPibEstados, reverse=True) #Realizo o rank, o sorted ordena pela primeira coluna da matriz, e coloco de forma reversa para ser o maior para o menor
print(rank)
#print(MedPibEstados)
tamRank = len(rank)
i=0
with open('D:/workspace/python/DesafioPython-Trainee/questao_02/saida_q2.txt','wt',encoding='utf-8') as q2: 
   q2.write("O ranking de estados por média de PIB per capita no ano de 2010 é respectivamente:\n")
   while i < tamRank:
      q2.write(str(i+1)+" lugar:\n"+str(rank[i][1])+"\n")
      i+=1

dataset.close()
q2.close()

"""
ESTADOS 

RO
AC
AM
RR
PA
AP
TO
MA
PI
CE
RN
PB
PE
AL
SE
BA
MG
ES
RJ
SP
SC
RS
MT
GO
DF

"""