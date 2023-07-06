import numpy as n


a = []
b = int(input('Qnt: '))
print('Dados:')
for i in range(0, b):
  c = int(input(''))
  a.append(c)

lin = int(input('qnt linhas: '))
col = int(input('qnt colunas: '))

mt = n.array(a)
print(mt)
mt = mt.reshape(lin,col)

media = mt.mean(1)
print(f'medias por linha: {media.reshape(col,1)}')
mediaT = mt.mean()
print(f'media total: {mediaT}')


SQTr = (media - mediaT)**2
SQTr = (SQTr.sum())*col
print(f'SQTr: {SQTr}')

SQT = (mt-mediaT)**2
print(f'SQT: {SQT.sum()}')

SQE = SQT.sum() - SQTr.sum()
print(f'SQE: {SQE}')

QMTr = SQTr/(col-1)
print(f'QMTr: {QMTr}')
QME = SQE/(lin*(col-1))
print(f'QME: {QME}')

F = QMTr/QME
print(f'F de Snedecor: {F}')
