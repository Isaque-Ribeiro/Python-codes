# CODIGO GERA CPF
# import random as r

cpf = []
str = ""

for i in range(9):
  cpf.append(r.randint(0,9))

L = 0
for i in range(9):
  L = (10-i)*cpf[i]

rd10 = L%11

if (rd10 == 0 or r == 1):
  cpf.append(0) 
else:
  cpf.append(11-rd10)

M = 0
for i in range(9):
  M = (10-1)*cpf[i+1]

rd11 = M%11

if(rd11 == 0 or rd11 == 1):
  cpf.append(0)
else:
  cpf.append(11-rd11)

j=1
for i in range(9):
  if i == 3 or i == 6:
    print ('.', end="")
  print(cpf[i], end="")
print (f'-{cpf[9]}{cpf[10]}')
