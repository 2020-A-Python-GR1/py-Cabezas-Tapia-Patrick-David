#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:57:38 2020

@author: d
"""


#b_series.py

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4) 

np_numeros= np.array((1,2,3,4))

series_a = pd.Series(lista_numeros)
series_b = pd.Series(tupla_numeros)
series_c = pd.Series(np_numeros)
#serie de todo un poco..
series_d=pd.Series([
    True,
    False,
    12,
    12.12,
    "Patrick",
None,
(1),
[2],
{"nombre":"Patrick"}    
    ])
print(series_d[3])

lista_ciudades=[
    "ambato",
    "cuenca",
    "loja",
    "quito"]

series_ciudades=pd.Series(
    lista_ciudades,
    index=[
        "A",
        "C",
        "L",
        "Q"])

print(series_ciudades[:])

valores_ciudad={
    "ibarra":9500,
    "Guayaquil":10000,
    "cuenca":2000,
    "loja":300
    }
series_valor_ciudad=pd.Series(
    valores_ciudad)


ciudades_menor_5k=series_valor_ciudad<5000
print(type(series_valor_ciudad))
print(type(ciudades_menor_5k))
print(ciudades_menor_5k)

series_valor_ciudad=series_valor_ciudad*1.2

series_valor_ciudad["loja"]=series_valor_ciudad["loja"]-50



ciudades_uno = pd.Series({
    "montanita":300,
    "guayaquil":1000,
    "quito":2000    
    })
ciudades_dos=pd.Series({
    "loja":300,
    "guayaquil":1000})
ciudades_uno["loja"]=0

print(ciudades_uno+ciudades_dos)


ciud_concat = pd.concat([
    ciudades_uno,
    ciudades_dos])

#add()
#sub()
#mul()
#div()

#append()



print(ciudades_uno.max())
print(pd.Series.max(ciudades_uno))
print(ciudades_uno.min())
print(np.max(ciudades_uno))

print(ciudades_uno.min())
print(pd.Series.min(ciudades_uno))
print(np.min(ciudades_uno))



print(ciudades_uno.mean())
print(ciudades_uno.median())
print(np.average(ciudades_uno))

print(ciudades_uno.head(2))
print(ciudades_uno.tail(2))

print(ciudades_uno.sort_values(
    ascending=False).head(2))

# 0 1000 5%
# 1001 - 5000 10%
# 5001 - 20000 15%

def calcular(valor_serie):
    if(valor_serie <= 1000):
        return valor_serie * 1.05
    if(valor_serie > 1000 and valor_serie <= 5000):
        return valor_serie * 1.10
    if(valor_serie>5000):
        return valor_serie * 1.15
ciudades_calculada = ciudades_uno.map(calcular)



#if else
#ciudades no cummple condicion aplica

ciudades_uno.where(ciudades_uno<1000,ciudades_uno * 1.05)


serries_numeros = pd.Series(['1.0','2',-3])
series_numeros_err= pd.Series(['not have','2',-3])
#print(pd.to_numeric(serries_numeros))

#ignore, coerce, raise (default)
print(pd.to_numeric(series_numeros_err,errors='coerce'))


