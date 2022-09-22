 
from calendar import day_abbr
import datetime
from distutils.log import error
import os
import sys

info ={}

while True:

    try:
        datainput=input("Informe a data ( DD/MM/AAAA):")  
        data=datetime.datetime.strptime(datainput,"%d/%m/%Y").date()  
        #print("data informada "+data.strftime('%d/%m/%Y')) 
        info["data"] = data.strftime('%d/%m/%Y')
        break
    except ValueError:
        print("A data informada é invalida")
        continue
        #os.system('python C:\Users\IARTES 07\Documents\GitHub\Python\modulo_python\TelefoneData.py')
    except:
        print("Erro ao inserir data")
        continue
        #os.system('python C:\Users\IARTES 07\Documents\GitHub\Python\modulo_python\TelefoneData.py')

while True:
    telefone= input("Informe telefone ( (92)00000-0000 ):")
    if len(telefone) == 14:
        if telefone[0] =='(' and telefone[3] ==')' :
            if telefone[9] == '-':
                info["telefone"] = telefone
                break
    else:
        print("Telefone digitado de forma incorreta")
        continue

print(info)


