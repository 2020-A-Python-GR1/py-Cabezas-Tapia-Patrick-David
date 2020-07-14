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
