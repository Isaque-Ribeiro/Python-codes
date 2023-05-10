# CRIPTOGRAFIA CESAR CYPHER

import random as r

text = input("Text to be encrypted: ")
text.lower()
crip = list(text)


k = r.randint(1,25)


for i in range(len(crip)):
    if (ord(crip[i])+k > 122):
      crip[i] = chr(ord(crip[i])- 26 + k)
    if(crip[i] == ''):
      crip[i] = ''
    if(ord(crip[i])>96 and ord(crip[i])<123):
        crip[i] = chr(ord(crip[i]) + k)

for i in crip:
  print (i , end='')