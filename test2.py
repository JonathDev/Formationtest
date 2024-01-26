import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns ; sns.set()

url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/spotify.zip"
df_music = pd.read_csv(url)
print(df_music.head())

print(df_music['key'])

grouped_data = df_music.groupby(['genre' , 'key']).size().reset_index()
print(grouped_data)


## table de pivot ne marche pas 
pivot_table = grouped_data.pivot(index='genre', columns='key').fillna(0)
#print(pivot_table)

matrix_corr = pivot_table.corr()

print(matrix_corr)