#2. Qual o ranking de estados por média de PIB per capita no ano de 2010?

lista= []
MedPibEstado = []
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
   if lista[x][1]=="AM" and lista[x][0] == "2010":
      #print(lista[x][0]+":"+lista[x][1]+":"+lista[x][13])
      pib += float(lista[x][13])
      qt+=1
   x+=1
   mediaPib = pib / qt
MedPibEstado.append(mediaPib)



print(MedPibEstado)



""" while x < tamanho:
   #print(lista[x])
   if lista[x][1] == "AC":
      print(lista[x][0]+":"+lista[x][13])
      pib += float(lista[x][13])
      qt+=1
   x+=1
mediaPibAC = pib / qt

MedPibEstado.append(mediaPibAC)

while x < tamanho:
   #print(lista[x])
   if lista[x][1] == "AM":
      print(lista[x][1]+":"+lista[x][13])
      pib += float(lista[x][13])
      qt+=1
   x+=1
mediaPibAM = pib / qt

MedPibEstado.append(mediaPibAM)

print(MedPibEstado) """

""" print(len(estados))

print(len(lista))

listEstados = len(estados) """
#print(estados)


""" def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lista = [1, 1, 2, 1, 3, 4, 3, 6, 7, 6, 7, 8, 10 ,9]

lista = remove_repetidos(lista)
print (lista) """

#mediaPib



""" while x < listEstados:
    print(lista[x])
    if lista[x][1] == "RO":
        print(lista[x][1]+":"+lista[x][13])
        pib += float(lista[x][13])
        qt+=1
    x+=1


mediaPib = pib / qt 

print(mediaPib) """
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