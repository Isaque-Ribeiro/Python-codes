'''NOTAS SECUNDARIAS'''
# https://colab.research.google.com/drive/1XGnDH2ZB1v3daMYtwO7sXvigjPdtKh7_?authuser=1#scrollTo=oGLNGmg_Xp4y
# https://replit.com/join/gakarsznfk-renata-mouramou
# códigos de uso dos métodos 

"""NOTAS DE NUMPY"""
     #ACESSO DE MATRIZES
# m.ndim - numero de dimensões: n

# m.shape - Formato (x,y)

# m.size - Quantidade de elementos (x*y)

# m.dtype - O tipo dos elementos ‘int32’

# m = [[array], [array], [array]]  -> mndarray = np.array(m)

# m[a:b,c:d] -> seleciona itens da linha 'a' até 'b' e colunas 'c'até'd'

     #FUNÇOES NUMPY -> import numpy as np

# np.array([listas]) - cria um array de listas

# np.arrage(inicio, fim, passo) - criar um array sequencial com passo

# np.zeros((linhas, colunas)) - definir uma matriz preenchida com zeros

# np.ones((linhas, colunas)) - gerar uma matriz preenchida com numeros 1

# np.zeros_like() - gera 0s no fomrato do parâmetro (matriz, array, etc)

# np.ones_like() - gera 1s no fomrato do parâmetro (matriz, array, etc)

# np.linspace(inicio, fim, size) - array igualmente espaçado dentro do intervalo

# np.random.randint(min, max, (matriz)) - matriz de arrays aleatorios

# np.dot - multiplicação de matrizes

# np.linalg.inv(matriz) -> recebe o inverso do número de cada posição 

# np.linalg.det(matriz ) -> determinante

# matriz.transpose() / matriz.T -> matriz transposta

# MATRIZ BOOLEANA
# a = np.arange(0,6)
# sel = a>=3
# b = a[sel]

'''também vale para os eixos a=0 colunas, a=1 linhas'''
# matriz.max/min() -> retorna o máximo/mínimo da matriz ou os máximos/mínimos do eixo 'a'
# matriz.cumsum() -> soma cumulativa
# matriz.mean() -> media da matriz
# matriz.std() -> desvio padrão da matriz

# fom scipy.special import fatorial
# a = np.array(x)
# fatorials = fatorial(a)

'''matplotlib'''
#PONTOS NO GRÁFICO
  # x = np.arange(0,20)
  # y = np.random.randint(0,10,(20))
  # plt.scatter(x,y)
  # plt.show()

#PLOT (LIGAMENTO DE PONTOS)
  # x = np.arange(0,20)
  # y = np.random.randint(0,10,(20))
  # plt.plot(x,y,'ro', linewidth=1)
  # (abscissa,ordenada, 'inicial da cor e 'o', tamanho do ponto)
  # plt.show()

#GRAFICO DE BARRAS (VERTICAL)
  # x = np.arange(0,20)
  # y = np.random.randint(0,10,(20))
  # plt.bar(x,y)
  # plt.show()

#GRAFICO EM PIZZA
  # x = np.arange(0,20)
  # y = np.random.randint(0,10,(20))
  # plt.pie(x)
  # plt.show()
  # x**(a)
#PLOT DE N GRAFICOS - SUBPLOTS
  # Plt.subplot(2,2,N)
  # x = np.arange(-20,21)
  # plt.subplot(2,2,1)
  # plt.plot(x,x)
  # plt.subplot(2,2,2)
  # plt.bar(x,x**2)
  # plt.subplot(2,2,4)
  # plt.scatter(x,x**3,linewidth = 3)
  # plt.show()
            # OU
  # x = np.linspace(-1,1,100)
  # for i in range(1,7):
  # plt.subplot(2,3,i)
  # plt.plot(x,x**i)
  # plt.title(f'AAAAAA{i} AAAAA ')
  # plt.show()

#APLICAÇÕES
   #https://colab.research.google.com/drive/1gLBC6iHUtJ95HPYxzi6wc7LQUM2WGePY?authuser=2#scrollTo=dBA4D2qy74EN
