import os
os.system('cls')

"""
LER, CRIAR E MODIFICAR ARQUIVOS

'r' -> Usando somente para ler algo
'w' -> Usado somente para escrever algo
'r+' -> Usado para ler e escrever algo
'a' -> Usado para acrescentar algo

"""

#NOME COMPLETO: JOAO PAULO REIS MARQUES
#EMAIL'S: joaopaulo-rm@hotmail.com | joaopaulo.rm7@gmail.com


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
   if lista[x][0] == "2010" and lista[x][3]=="Manaus": #impressão para ver como ficou os dados
      print(lista[x])

   x+=1 

#Reescrevo no documento
""" with open('D:/workspace/python/DesafioPython-Trainee/dataset/pib_modificado','wt',encoding='utf-8') as dataset: 
      dataset.write(str(lista))
#Prova Real das Modificações
 """

#print(lista[1][3])


#Usei este metodo para saber qual o endereço de cada informação na base de dados
""" texto = "Ano,Sigla da Unidade da Federação,Nome da Unidade da Federação,Nome do Município,Nome da Região Geográfica Intermediária,Hierarquia Urbana,Valor adicionado bruto da Agropecuária a preços correntes (R$ 1.000),Valor adicionado bruto da Indústria a preços correntes (R$ 1.000),Valor adicionado bruto dos Serviços a preços correntes (R$ 1.000),Valor adicionado bruto da Administração a preços correntes (R$ 1.000),Valor adicionado bruto total a preços correntes (R$ 1.000),Impostos, líquidos de subsídios, sobre produtos a preços correntes (R$ 1.000),Produto Interno Bruto a preços correntes (R$ 1.000),Produto Interno Bruto per capita a preços correntes (R$ 1.00)"
txt = texto.split(",") 
print(txt[10])
print(len(txt)) """

dataset.close()
