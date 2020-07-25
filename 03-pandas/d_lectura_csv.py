#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:57:38 2020

@author: d
"""


#b_series.py

import pandas as pd
import os

path = "/home/d/Documentos/programacion/py-cabezas-tapia-patrick-david/03-pandas/data/artwork_data.csv"

df1 = pd.read_csv(
    path,
    nrows=10)



columnas = ['id', 'artist', 'title',
            'medium', 'year',
            'acquisitionYear', 'height',
            'width', 'units']

df2 = pd.read_csv(
    path,
    nrows=10,
    usecols = columnas)



df3 = pd.read_csv(
    path,
    usecols = columnas,
    index_col = 'id')

# artwork_data.pickle
path_guardado  = "/home/d/Documentos/programacion/py-cabezas-tapia-patrick-david/03-pandas/data/artwork_data.pickle"

df3.to_pickle(path_guardado)

df4 = pd.read_pickle(path_guardado)

