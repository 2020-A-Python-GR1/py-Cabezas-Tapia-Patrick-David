#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:31 2020

@author: d
"""
import pandas as pd

# g_iloc_loc.py

path_guardado  = "/home/d/Documentos/programacion/py-cabezas-tapia-patrick-david/03-pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

#loc
#el loc sirve para filtrar por lables
'''

primero = df.loc[1035]
primero_data = pd.DataFrame(primero)
print(primero)
print(type(primero))
segundo = df.loc[1035,'artist']
print(segundo)
print(type(segundo))    


cuarto = df.loc[[1035,1036],['artist','medium']]
tercero = df.loc[1035,['artist','medium']]
print(tercero)
print(type(tercero))


cinco = df.loc[1035:1037,'artist':'medium']

#filtrado por en indice

df_1035 = df[df.index==1035]'''



#filtrar por indices
#iloc 
tercero = df.iloc[0]
tercero = df.iloc[[0,10]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]
#filtrado de indice por rango
tercero = df.iloc[0:10,0:4]

print(len(tercero))

