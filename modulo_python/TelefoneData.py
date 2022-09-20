
"""
#Condições Telefone

1.

#Condições Data
1. dias entre de 1 a 31
2. mes de 1 a 12




"""
""" 
import datetime 

dia:int
mes:int
ano:int



dia = int(input())
mes = int(input())
ano = int(input())

"""

 
from calendar import day_abbr
import datetime
from distutils.log import error
import os

info ={}

try:
    datainput=input("Informe a data ( DD/MM/AAAA) ")  
    data=datetime.datetime.strptime(datainput,"%d/%m/%Y").date()  
    print("data informada "+data.strftime('%d/%m/%Y')) 
    print(data.strftime('%d'))

    info["data"] = data.strftime('%d/%m/%Y')
except ValueError:
    print("A data informada é invalida")
    os.system('python C:\Users\IARTES 07\Documents\GitHub\Python\modulo_python\TelefoneData.py')
except:
    print("Erro ao inserir data")
    os.system('python "C:\Users\IARTES 07\Documents\GitHub\Python\modulo_python\TelefoneData.py"')


info["telefone"] = "(92)999999999"

print(info)

"""
if data.day >= 1 and data.day <=31 :
    print("true")
else:
    print("Error, dia invalido")

if data.month >= 1 and data.month <=12:
    print("true")
else:
    print("mes invalido")
"""






