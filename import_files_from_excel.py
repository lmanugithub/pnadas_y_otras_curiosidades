# An example to import multiples files with multiples sheets of Excel

# Importando librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Insert the directory
import sys
import os

# This lines ares to use in Colaboratory
from google.colab import drive
drive.mount('/content/drive')

ruta = './data_files/'

files = [file for file in os.listdir(ruta)]
files.sort()
temp_dict = {}
df_sheet1 = pd.DataFrame()
df_sheet2 = pd.DataFrame()
df_sheet3 = pd.DataFrame()

for file in files:
    xl_file = pd.ExcelFile(ruta + file)

    for sheet_name in xl_file.sheet_names:
        temp_dict[sheet_name] = xl_file.parse(sheet_name)
        sheets=list(temp_dict.keys())
        print(sheets)
        
    try:
        if not temp_dict.get(sheets[0]).empty:
            df1 = pd.DataFrame(temp_dict.get(sheets[0]))
            df_sheet1 = pd.concat([df_sheet1, df1])

        if not temp_dict.get(sheets[1]).empty:
            df2 = pd.DataFrame(temp_dict.get(sheets[1]))
            df_sheet2 = pd.concat([df_sheet2, df2])

        if not temp_dict.get(sheets[2]).empty:
            df3 = pd.DataFrame(temp_dict.get(sheets[2]))
            df_sheet3 = pd.concat([df_sheet3, df3])
    except IndexError as ie:
        print(ie)

    temp_dict = temp_dict.clear()
    sheets = sheets.clear()
    xl_file = ''
