#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:34:10 2020

@author: d
"""

import pandas as pd

#cargar el pickle

path_guardado  = "/home/d/Documentos/programacion/py-cabezas-tapia-patrick-david/03-pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

#selecionar una sola colupna de un dataframe

serie_artistas_dup = df['artist']

artistas = pd.unique(serie_artistas_dup)
print(type(artistas))
print(artistas.size)

blake = df['artist'] == 'Blake, William'    #se combierte en una serie
df_blake = df[blake]
print(blake.value_counts())
print(len(df_blake))



