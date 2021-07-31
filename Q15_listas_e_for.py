#!/usr/bin/env python
# coding: utf-8

# In[ ]:


i = 0
while i < n:
    nota = float(input('Nota: '))
    lista_nota.append(nota) 
    i += 1

media = sum(lista_nota)/len(lista_nota)
media = round(media, 2)


lista_media.append(media)

media_TF = 0
if media > 5:
    media_TF = 'True'
else:
    media_TF = 'False'


lista_media_TF.append(media_TF)

count += 1

lista = [lista_nome, lista_idade, lista_nota, lista_media, lista_media_TF]
print(lista)

