

      
      
#1

"""
print("Numero 1")
var1 = int(input())
print("Numero 2")
var2 = int (input())

print("Numeros digitados")
print(var1)
print(var2)

"""



#2 Seja x = 2 + 4j, qual é tipo associado a essa variável pelo interpretador

"""
x = 2+4j

print(type(x)) #<class 'complex'>


#3

urnas = {} 
sessao = {"escola municipal", 103}
print(type(urnas)) #<class 'dict'>
print(type(sessao))#<class 'set'> ou Conjunto
"""


"""
4. Nas definições de nomes de variáveis abaixo quais têm nomes válidos e quais são invalidos
    1. ola = "mundo" # Valido
    2. _ola = "mundo" # Valido
    3. _1_ola = "mundo" # valido
    4. 1_ola = "mundo" # Invalido SyntaxError: invalid decimal literal
    5. ola_1 = "mundo"  # Valido
    6. meu mundo = "ola" # Invalido Não pode ter espaço

aponte as razões para os nomes inválidos, indicando o item e a razão da violação
das regras de nomeação de variável.

5. No seguinte comando de atribuição 
   1. casa, senha = "minha", "ola" # Funcionou
   2. casa, senha = "minha" # esperava duas atribuições mas so teve uma.
   3. casa = "minha" # Funcionou

Quais foram as atribuições que funcionaram e quais não funcionaram? Explique a razão dos problemas.

6. Considere as seguintes operações matemáticas, e indique o resultado de cada uma:
   1. (10 - 6)**2 # 16
   2. 10 - 6**2 # - 26
   3. 10 - 3 // 2 #9
   4. 10 - 3 / 2 #8.5


7. Qual a importância de se criar ambiente virtuais para o desenvolvimentos de projetos usando Python?
R= um ambiente virtual empacota todas as dependências que um projeto precisa e armazena em um diretório, 
fazendo com que nenhum pacote seja instalado diretamente no sistema operacional. 
Sendo assim, cada projeto pode possuir seu próprio ambiente e, consequentemente, suas bibliotecas em versões específicas.


8. Descubra e responda qual versão do python está instalado no seu ambiente de desenvolvimento. Que comando você usou 
para obter essa informação?
#
Python 3.10.7
python --version


9. Uma tupla é um tipo imutável, portanto qualquer variável desse tipo pode ser alterada desde que os seus elementos 
sejam individualizados, como no código abaixo:

   __comprado = ("carro", "GM", "20K")__

   __comprado[1] = "Ford"__

   você concorda com essa afirmação? justifique sua resposta.

   R= TUPLAS NAO TEM METODOS PARA MODIFICAÇÕES


10. Considere o código abaixo:

      __numero = input()__
      
      print(numero*3)
   
      se o valor 3(três) for informado como entrada e armazenado na variável número.
      R= Ele vai imprimir 333, por considerar a entrada uma String
      
      """




numero = input()
      
print(numero*3)