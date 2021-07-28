#!/usr/bin/env python
# coding: utf-8

# In[ ]:


lista_onze = []
y = 11
for i in range(len(lista)):
    onze = lista[i] * y
    lista_onze.append(onze)
    y -= 1
    if (y == 1):
        break


    resto_soma2 = (sum(lista_onze)*10)%11
    if resto_soma2 == lista[10]:
        print('CPF válido :)')

