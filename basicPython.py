"""
Revisão - P1
"""
#Input
str = input('')
int = int(input(''))
float = float(input(''))

#Print
nome = 'Isaque'
idade = '19'
altura = 1.70
print('A idade do', nome, 'é', idade, 'e a sua altura é', altura)
print(f'A idade do {nome} é {idade} e a sua altura é{altura}')




#string 
#join() - Esse comando serve para unir as strings de uma lista
palavras = ['olá', 'mundo', 'como', 'vai']
frase = ' '.join(palavras)
print(frase)  # saída: 'olá mundo como vai'
frase = ', '.join(palavras)
print(frase)  # saída: 'olá, mundo, como, vai'

#split() - Esse comando serve para dividir uma string em uma Lista
frutas = "banana,maçã,uva"
lista_frutas = frutas.split(",")
print(lista_frutas) #["banana", "maçã", "uva"]
texto = "Isso é um exemplo"
lista_palavras = texto.split(3)
print(lista_palavras) #["Iss", "o é", " um", " ex", "emp", "lo"]

#fateamento de string - string[inicio:fim]
string = "abcdefghij"
print(string[2:5])   # resultado: "cde"
print(string[:5])    # resultado: "abcde"
print(string[7:])    # resultado: "hij"
print(string[1:8:2])   # resultado: "bdfh"






#operadores aritmeticos
    # Adição (+)
    # Subtração (-)
    # Multiplicação (*)
    # Divisão (/)
    # Divisão inteira (//)
    # Resto da divisão ou módulo (%)
    # Potenciação (**)

#comando if
    #operadores:
        # Igual (==)
        # Diferente (!=)
        # Menor (<)
        # Maior (>)
        # Menor igual (<=)
        # Maior Igual (>=)
        # e (and)
        # ou (or)




#comandos de Loop
#for
for i in range(1, 6, 1): #(inicio, fim, passo) ele não vai até o 6
    print(i)
    
lista = [1, 2, 3, 4, 5]
for i in lista:
    print(i)
    
dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
for i in dicionario:
    print(i) 
    #Vai imprimir: 
        #chave1
        #chave2
        #chave3

for i in dicionario.keys():
    print(i) 
    #Vai imprimir: 
        #chave1
        #chave2
        #chave3

for i in dicionario.values():
    print(i)
    #Vai imprimir: 
        #valor1
        #valor2
        #valor3

for i, j in dicionario.items():
    print(i, j)
    #Vai imprimir: 
        #chave1 valor1
        #chave2 valor2
        #chave3 valor3

    #comando zip
a = [1, 2, 3]
b = ['a', 'b', 'c']
c = [True, False, True]

for x, y, z in zip(a, b, c):
    print(x, y, z)
    #vai imprimir:
        #1 a True
        #2 b False
        #3 c True

    #comando enumerate
lista2 = ['a', 'b', 'c', 'd']
for i, elemento in enumerate(lista2):
    print(i, elemento)
    #vai imprimir:
        #0 a
        #1 b
        #2 c
        #3 d


#Lista

lista.append() #adciona um objeto a lista

lista.clear() #remove todos os elementos da lista

lista.copy()
lista_original = [1, 2, 3, 4]
lista_copia = lista_original.copy()

lista_copia.append(5)
print(lista_original) # saída: [1, 2, 3, 4]
print(lista_copia) # saída: [1, 2, 3, 4, 5]

lista.extend() # acopla listas
listaImpar = [1, 3 , 5, 7]
listaPar = [2, 4, 6, 8]
listaImpar.extend(listaPar) #listaImpar: [1, 3, 5, 7, 2, 4, 6, 8]

novaLista = zip(listaImpar, listaPar) # [(1, 2), (3, 4), (5, 6), (7, 8)]

lista.count()#retorna o elemento na posição
lista = [1, 2, 3, 2, 4, 2]
lista.count(2) #retorna o 3

lista.insert() #(index, objeto) - Insere um elemento em um detrminado index
frutas = ['banana', 'maçã', 'laranja']
frutas.insert(2, 'pera') #frutas: ['banana', 'maçã', 'pera',  'laranja']

lista.pop() #remove e retorna o ultimo elemento da lista, caso seja adicionado o Index ele remove e retorna o elemento do index
frutas = ['banana', 'maçã', 'laranja']
laranja = frutas.pop()
print(laranja)  # saída: "laranja"
print(frutas)  # saída: ["banana", "maçã"]


lista.remove() #remove um elemento
lista = [1, 2, 3, 4, 5]
lista.remove(3)
print(lista) # saida: [1, 2, 4, 5]

#listcomprehension - cria uma lista a partir de uma lista existente ou outra sequência já existente
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in numeros if num % 2 == 0]

#copias
a = b # a e b referentes ao mesmo espaço de memoria
a = b[;] # a copia b tomando posiçoes de memoria diferentes





#dicionarios
dicionario.copy() #Copia o dicionario

dicionario.clear() #limpa o dicionario - exclui tudo

dicionario.pop() #(chave) remove e retorna uma chave

dicionario.popitem() # (chave,valor) remove e retorna um item dentro de uma chave

dicionario.update() #

#funções
def definição():

def variaveis(a, b):
    return a*b

def encapsulamento (*a): #possibilida flexibilidade de elementos entrada

#multiplas saídas
def quadrado_E_cubo(x):
    quadrado = x ** 2
    cubo = x ** 3
    return [quadrado, cubo]

valores = quadrado_E_cubo(3)
print(valores)  # Saída: [9, 27]

#bibliotecas
import math
import random
import time


# usar dicionário para direcionar funções dentre casos distintos

def funcao1():
    print("Função 1")

def funcao2():
    print("Função 2")

def funcao3():
    print("Função 3")
opcoes = {
    1: funcao1,
    2: funcao2,
    3: funcao3
}


# LEITURA DE ARQUIVOS
  #criando objeto
   open(arquivo, acesso)

  #acessos
    #r - modo de leitura
      leitura = open(arquivo, r)
    #r+ - modo de leitura e escrita
    # w - modo de escrita
      escrita = open(arquivo, w)
    # w+ - modo de leitura e escrita
    # a - modo de apend
    # a+ - modo de apend e leitura

  #metodos do objeto
    arquivo.read(n) #lê n bytes em forma de string
    arquivo.readlines(n) #lé n linhas do arquivo.  Se n não for declarado, le
    arquivo.readlines() #le todas as linhas do arquivo e organiza em uma lista
    arquivo.write(str) #escreve a string (str) no arquivo
    arquivo.writelines(lstr_list)#escreve todas as strings contidas na lista
