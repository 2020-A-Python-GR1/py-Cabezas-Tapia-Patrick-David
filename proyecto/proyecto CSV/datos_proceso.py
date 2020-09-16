import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

path = '/home/d/Documentos/programacion/py-cabezas-tapia-patrick-david/proyecto/proyecto CSV/MoviesOnStreamingPlatforms_updated.csv'
df = pd.read_csv(path)
columns_name = ['Unnamed: 0', 'ID', 'Title', 'Year', 'Age', 'IMDb', 'Rotten Tomatoes', 'Netflix', 'Hulu', 'Prime Video', 'Disney+', 
'Type', 'Directors', 'Genres', 'Country', 'Language', 'Runtime']
# print(df1.columns)
# print(columns_name)

# x = len(df1['Rotten Tomatoes'].value_counts()[:10])
# df_columnas = ['Title','IMDb']
# print(df1.sort_values(by='IMDb', ascending = False).head(30))

# print(df1[df1['Rotten Tomatoes']=='100%']['Directors'].value_counts()[df1[df1['Rotten Tomatoes']=='100%']['Directors'].value_counts()>1])

# print(df['Runtime'].value_counts().sort_values(ascending = False))
# print(df['IMDb'][df['Netflix']==1].value_counts())
# print(df['Netflix']==1)

# valores = df[df['Netflix']==1][df['Disney+']==1][df['Prime Video']==1]
for i in df['']:
    print(i)

# valores
# print(valores[:30])