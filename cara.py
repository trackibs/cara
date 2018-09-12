import pandas as pd
import numpy as np
from datetime import datetime
import csv
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('export.csv', na_values='')
pd.set_option('display.max_rows', 1000)

df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace('\s+', '_')

df.fillna('', inplace=True)

df = df[df.Tracking != 'Symptom Score']
df['Date'] = pd.to_datetime(df['Date'])
df.index = df['Date']
del df['Date']

df['type1'] = np.where(df['String_Value'].str.contains('Type 1'), 1, 0)
df['type2'] = np.where(df['String_Value'].str.contains('Type 2'), 1, 0)
df['type3'] = np.where(df['String_Value'].str.contains('Type 3'), 1, 0)
df['type4'] = np.where(df['String_Value'].str.contains('Type 4'), 1, 0)
df['type5'] = np.where(df['String_Value'].str.contains('Type 5'), 1, 0)
df['type6'] = np.where(df['String_Value'].str.contains('Type 6'), 1, 0)
df['type7'] = np.where(df['String_Value'].str.contains('Type 7'), 1, 0)

df = df.groupby(df.index.date).sum()

print(df)

bristol_colors = ["#000000", "#333300", "#663300", "#996600", "#cc9900", "#ff9900", "#ff0000"]
df[['type1','type2','type3','type4','type5','type6','type7']].plot.bar( stacked=True, title='BM Count grouped by Bristol Type', color=bristol_colors)

mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

plt.tight_layout()
plt.savefig('Cara.png', bbox_inches='tight')
plt.show()
