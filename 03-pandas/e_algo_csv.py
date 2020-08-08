#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:26:56 2020

@author: d
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado  = "/home/d/Documentos/programacion/py-cabezas-tapia-patrick-david/03-pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()

path_excel  = "/home/d/Documentos/programacion/py-cabezas-tapia-patrick-david/03-pandas/data/artwork_data.xlsx"
sub_df.to_excel(path_excel)

path_excel_indice  = "/home/d/Documentos/programacion/py-cabezas-tapia-patrick-david/03-pandas/data/artwork_data2.xlsx"
path_excel_columnas  = "/home/d/Documentos/programacion/py-cabezas-tapia-patrick-david/03-pandas/data/artwork_data3.xlsx"

columnas = ['artist','title','year']
sub_df.to_excel(path_excel_columnas,columns=columnas)
sub_df.to_excel(path_excel_indice,index=False)


path_excel_mt  = "/home/d/Documentos/programacion/py-cabezas-tapia-patrick-david/03-pandas/data/artwork_data_mt.xlsx"
writer = pd.ExcelWriter(path_excel_mt, engine='xlsxwriter')
sub_df.to_excel(writer,sheet_name='Primera')
sub_df.to_excel(writer,sheet_name='Segunda')
sub_df.to_excel(writer,sheet_name='Tercera')
writer.save()

# Formato condicional #

num_artistas = sub_df['artist'].value_counts()
path_excel_colores = "/home/d/Documentos/programacion/py-cabezas-tapia-patrick-david/03-pandas/data/artwork_data_mt.xlsx"
# artwork_data_colores.xlsx

writer = pd.ExcelWriter(path_excel_colores,
                            engine='xlsxwriter')
# Series

num_artistas.to_excel(writer,sheet_name = 'Artistas')

# Seleccionando la hoja de trabajo

hoja_artistas = writer.sheets['Artistas']

ultimo_numero = len(num_artistas.index) + 1

# rango_celdas = 'B2:B{}'.format()

rango_celdas = f'B2:B{ultimo_numero}'
rango_celdas_c = f'C2:C{ultimo_numero}'
# Formato

formato_artistas = {
        "type": "2_color_scale",
        "min_value": "10",
        "min_type": "percentile",
        "max_value": "99",
        "max_type": "percentile"}

hoja_artistas.conditional_format(rango_celdas,formato_artistas)
hoja_artistas.conditional_format(rango_celdas_c,formato_artistas)
writer.save()



'''
workbook = xlsxwriter.Workbook('chart_line.xlsx')
worksheet = workbook.add_worksheet()

# Add the worksheet data to be plotted.
data = [10, 40, 50, 20, 10, 50]
worksheet.write_column('A1', data)

# Create a new chart object.
chart = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart.add_series({'values': '=Sheet1!$A$1:$A$6'})

# Insert the chart into the worksheet.
worksheet.insert_chart('C1', chart)

workbook.close()
'''

### SQL


with sqlite3.connect("bdd_artist.bdd") as conexion:
    sub_df.to_sql('py_artistas',conexion)
    
    
# json
    
sub_df.to_json('artistas.json')
sub_df.to_json('artistas_tabla.json', orient = 'table')
    















