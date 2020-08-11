#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:17:03 2020

@author: d
"""
import pandas as pd
import xlsxwriter

path_guardado  = "/home/d/Documentos/programacion/py-cabezas-tapia-patrick-david/03-pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()
num_artistas = sub_df["artist"].value_counts()


workbook = xlsxwriter.Workbook('grafica_valores.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write_column('A1', num_artistas.index)
worksheet.write_column('B1', num_artistas)

chart = workbook.add_chart({'type': 'line'})


chart.add_series({
    'name':       'Number of Artists',
    'categories': '=Sheet1!$A$1:$A$85',
    'values':     '=Sheet1!$B$1:$B$85',
 
})

chart.set_y_axis({'name': 'Number'})
chart.set_x_axis({'name': 'Artists'})


worksheet.insert_chart('D2', chart)



workbook.close()


