import random
import os

os.system('cls')
#print("Oi mundo") # aula 1 
# O terminador de comando do python são os Enter's/quebra de linha
# entretanto se quiser mais de um comando na mesma linha, devesse
# finalizar os comandos com ';'

# Variaveis Globais são declaradas fora das funções ou sendo antecedidas da
# palavra reservada " global" e inicializa ela em outra linha
# int(float) -> retorna a parte inteira do valor
# float(int)
#num = rando.randrange(valor iniciar, valor final)
"""
num = 1
nome = "Joao Paulo"


x = 1 #Int
y = "Oi Mundo" # String 'str'
valor = 1.5 #float
booleano = True #True or False, bool
n1 = 5; n2 = 2; var = complex(1j) # Numeros complexos
lista = ["casa", "carro","PC","Internet", 1., 58.3] # Arrey
lista = ("casa", "carro","PC","Internet", 1., 58.3) #Tupla, não é possivel substituir elementos
rage = range(0,100) #cria elementos de 1 a 100
dicio = { # Dictionary
    "nome":"joao paulo"
    "idade": 22
    "nacionalidade":"Brasileiro"
}
sett = {2,34,4,0,4,5,5,6,7} #Ordena os valores, não repete valores
frozensett =frozenset({2,34,4,0,4,5,5,6,7})# sett bloqueado

print(lista[3])
print(var.real)
print(var.imag)


print ("Valor:"+str(lista[5]))
print("Tipo: "+str(type(lista))) # type retorna o tipo de dados do objeto

"""
"""
len(list) -> tamanho do arrey
strip -> retira espaços do inicio e do fim
lower -> converte a string para minusculo
upper -> converte a string para maiusculo 
replace -> substitui string ou caracter
split -> subdivisão de uma string pelo o indicador setado 
da para fazer combinações

frase = "   Vamos Pain, vamos ganhar       "
print (frase[3:13])
print(frase)
print (frase.strip().lower())
print (frase.strip().upper())
print (frase.replace("Pain","Vorax"))
a = frase.split
print(len(frase))

in / not in -> procura palavra

frase1 = "O importante não é vencer todos os dias"
frase2 = ",mas lutar sempre"

fraseCompleta= frase1+" "+frase2

#res ="Pain" in frase #procura palavra em uma frase
print(fraseCompleta)

# String format 
cidade = "Manaus"
dia = 10
mes = "Maio"
ano = 2021
nome = "Joao Paulo"
data = "{}, {} de {} de {} \n{} \"\""

# \' \" \n -> quebra de linha \r -> retorno(ENTER) \t -> tabulação(TAB) \b ->backspace 


print (data.format(cidade,dia,mes,ano,nome))


list.append("x") -> adiciona elemento na lista
list.remove("Palio")
list.pop("")
list.clear()



 # Aula sobre IF e Else

a = 100
b = 10
res = 0 
op = "/"

if op =="+":
    res = a+b

elif op =="-":
    res = a-b

elif op =="*":
    res = a*b

elif op =="/":
    res = a/b

else:
    print("Erro!")


print (str(a) + op + str(b) + "=" + str(res))




clima = "sol"
dinheiro = 299
lugar =""

if clima == "sol" and (dinheiro > 300 and dinheiro<500): # todas as condições tem que ser verdadeiras para ser aceito
    lugar = "clube"
else:
    lugar = "cinema"

print (lugar)

# and -> todas as condições tem que ser verdadeiras
# or -> se uma das condições for verdadeira, executa




# LOOPS (FOR E WHILE )

carros = ["jeep","gol","camaro","ford","honda"]

for x in carros: #informa a variavel que vai servir de indice e informa a lista que vai percorrer
    print(x)
    if(x=="camaro"):
        break #encerra o loop
        print("vw")

while (teste logico): # while precisa de um teste logico para indicar se ele continua a execução enquanto retornar verdadeiro
    comando 1
    comando 2
    comando x
i = 0
while i<9:
    print(i)
    i+=1



nome = input("Digite Nome: ") # input captura dados digitados por usuario
print(nome+" digitado")



# LIST
# TUPLAS -> NAO TEM METODOS PARA MODIFICAÇÕES

tupla=(1,2,3,4,5)

lista = list(tupla) # converte tupla para lista

lista[2]=100

tupla = tuple(lista)# converte lista para tupla

for x in tupla:
    print(x)



#  MATRIZES -> uma lista dentro de outra lista

Arrey = [
            [0,1]#
        ,   [2,3]#
        ,   [4,5]#
]

for l,c in Arrey:
    print(str(l) +" "+str(c))



# Dictionary-> Usa mesmo sistema que o json, de chave e valor
 
dicionario = {
        "nome":"valor"
    ,   "Operacao":"B.I"
    ,   "cor":"Azul Escuro"
}

dicionario2={
    "pessoa1":{
        "nome":"fulano",
        "idade":"21"
    },
    "pessoa2":{
        "nome":"fulano",
        "idade":"21"
    },
    "pessoa3":{
        "nome":"fulano",
        "idade":"21"
    }
}

#print(dicionario)
#cor = dicionario["cor"]
#op = dicionario.get("Operacao")
#print(dicionario["cor"] + " , "+ op)

#for x in dicionario:
    #print(x) #chaves
 #   print(dicionario[x]) # valores

for x,y  in dicionario.items():
    print(x +":"+y)


# Funções (def)
# toda alterção na função sera considerada quando ela for chamada
def subtrair():
    res = n1-n2
    print(res)

def calculos():
    somar()
    subtrair()

calculos()

# FUNÇÕES QUE RECEBEM VALORES DE ENTRADA

def somar(*n): 
    r = 0
    for x in n:
        r+=x

    print(r)

def textos(*t):# *n -> qauntidade qualquer de elementos 
    print(t[0])
    for x in t:
        print(x)


textos("Bemol","Treinee","Python")
somar(1,2,3)


# FUNÇÕES QUE RETORNAM VALORES  

def somar(*n): 
    r = 0
    for x in n:
        r+=x
    return r


print(somar(1,2,3,4,5,6,7,8,9))



# lambda -> função simples e anonima

soma = lambda a,b: a+b
exp = lambda a,b,c: (a+b)*c

print((lambda a,b: a+b)(1,2))
r=soma(1,2)

print(r)
print(soma(3,4))
print(exp(1,2,4))

res = lambda x,func: x + func(x)
resp = res(2,lambda x: x*x)
print(resp)




# TRY EXCEPTI
x=10
try:

    print(x)

except:
    print("Erro!")
else:
    print("Tudo certo")

#except NameError: # Executa se o try retornar erro
#    print("Variavel nao inicializada")
finally: # Executa se o try retornar erro ou nao
    print("Fim Tratamento")


num="Joao"
if not type(num) is int:
    raise Exception("Valor nao permitido")

#LER, CRIAR E MODIFICAR ARQUIVOS

'r' read -> Usando somente para ler algo
'w' write -> Usado somente para escrever algo
'r+' -> Usado para ler e escrever algo
'a' append -> Usado para acrescentar algo
'x' create -> criar
't' text ->
'b' binario 



arq=open('D:/workspace/python/aulas/teste.txt','r')
arq.write ("\n Treinee bemol 1")
arq.close()

arq=open('D:/workspace/python/aulas/teste.txt','rt')

#print(arq.read())
#print(arq.readline())
#print(arq.readline())

for l in arq:
    print(l)

arq.close()

# Replace ; por ,

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
#os.remove('D:/workspace/python/aulas/teste.txt')

texto = "Ano,Sigla da Unidade da Federação,Nome da Unidade da Federação,Nome do Município,Nome da Região Geográfica Intermediária,Hierarquia Urbana,Valor adicionado bruto da Agropecuária a preços correntes (R$ 1.000),Valor adicionado bruto da Indústria a preços correntes (R$ 1.000),Valor adicionado bruto dos Serviços a preços correntes (R$ 1.000),Valor adicionado bruto da Administração a preços correntes (R$ 1.000),Valor adicionado bruto total a preços correntes (R$ 1.000),Impostos, líquidos de subsídios, sobre produtos a preços correntes (R$ 1.000),Produto Interno Bruto a preços correntes (R$ 1.000),Produto Interno Bruto per capita a preços correntes (R$ 1.00)"
txt = texto.split(",")
print(txt[4])
print(len(txt))