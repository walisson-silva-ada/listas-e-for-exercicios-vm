#!/usr/bin/env python
# coding: utf-8

# In[ ]:


i = 0
while i < n:
    nota = float(input('Nota: '))
    lista_nota.append(nota) 
    i += 1
else:

n = int(input('Número de provas deve ser maior que 2, digite novamente:'))

i = 0
while i < n:
    nota = float(input('Nota: '))
    lista_nota.append(nota) 
    i += 1   





lista_nota2 = sorted(lista_nota)
lista_nota2.pop(0)
lista_nota2.pop(-1)



media = sum(lista_nota2)/len(lista_nota2)
media = round(media, 2)

lista_media.append(media)

media_TF = 0
if media > 5:
media_TF = 'True'
else:
media_TF = 'False'


lista_media_TF.append(media_TF)

count += 1

