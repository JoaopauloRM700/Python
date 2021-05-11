#import random
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
"""

